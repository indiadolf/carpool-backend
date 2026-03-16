from django.db import models
from users.models import User
from network.models import Node
from trips.models import Trip

from django.db.models.signals import post_save
from django.dispatch import receiver


class CarpoolRequest(models.Model):

    passenger = models.ForeignKey(User, on_delete=models.CASCADE)

    pickup_node = models.ForeignKey(Node, related_name="pickup", on_delete=models.CASCADE)

    drop_node = models.ForeignKey(Node, related_name="drop", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger} request"


class Offer(models.Model):

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    request = models.ForeignKey(CarpoolRequest, on_delete=models.CASCADE)

    detour = models.IntegerField()

    fare = models.FloatField()

    score = models.FloatField(default=0)

    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Offer for {self.request}"

@receiver(post_save, sender=CarpoolRequest)
def run_matching(sender, instance, created, **kwargs):

    if created:
        from .matching import match_request
        match_request(instance)

class Ride(models.Model):

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    passenger = models.ForeignKey(User, on_delete=models.CASCADE)

    pickup_node = models.ForeignKey(Node, related_name="ride_pickup", on_delete=models.CASCADE)

    drop_node = models.ForeignKey(Node, related_name="ride_drop", on_delete=models.CASCADE)

    fare = models.FloatField()

    def __str__(self):
        return f"{self.passenger} ride on {self.trip}"