from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [
        ("driver", "Driver"),
        ("passenger", "Passenger"),
    ]

    # 🔥 FIX: add default
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="passenger"
    )

    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    # optional but good for leaderboard
    rating = models.FloatField(default=5)

    def __str__(self):
        return self.username