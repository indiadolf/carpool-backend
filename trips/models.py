from django.db import models
from users.models import User
from network.models import Node


class Trip(models.Model):

    driver = models.ForeignKey(User, on_delete=models.CASCADE)

    start_node = models.ForeignKey(Node, related_name="trip_start", on_delete=models.CASCADE)

    end_node = models.ForeignKey(Node, related_name="trip_end", on_delete=models.CASCADE)

    route = models.JSONField()  
    # Example: ["A","B","C","D"]

    current_node = models.ForeignKey(Node, on_delete=models.CASCADE)

    route_index = models.IntegerField(default=0)

    max_passengers = models.IntegerField()

    current_passengers = models.IntegerField(default=0)

    started = models.BooleanField(default=False)

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trip {self.id} by {self.driver}"