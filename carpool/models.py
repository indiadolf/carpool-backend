from django.db import models
from users.models import User
from network.models import Node
from trips.models import Trip


class CarpoolRequest(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_node = models.ForeignKey(Node, related_name="pickup", on_delete=models.CASCADE)
    drop_node = models.ForeignKey(Node, related_name="drop", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Offer(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    request = models.ForeignKey(CarpoolRequest, on_delete=models.CASCADE)
    detour = models.IntegerField()
    fare = models.DecimalField(max_digits=8, decimal_places=2)
    score = models.FloatField(default=0)
    accepted = models.BooleanField(default=False)


# ✅ RIDE FIRST
class Ride(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_node = models.ForeignKey(Node, related_name="ride_pickup", on_delete=models.CASCADE)
    drop_node = models.ForeignKey(Node, related_name="ride_drop", on_delete=models.CASCADE)
    fare = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


# ✅ THEN RATING
class Rating(models.Model):
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE)

    passenger = models.ForeignKey(
        User,
        related_name="passenger_ratings",
        on_delete=models.CASCADE
    )

    driver = models.ForeignKey(
        User,
        related_name="driver_ratings",
        on_delete=models.CASCADE
    )

    score = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)