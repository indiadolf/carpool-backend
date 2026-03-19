from django.db import models
from users.models import User
from network.models import Node


class Trip(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    start_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="trip_start")
    end_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="trip_end")


    route = models.JSONField(default=list)


    current_index = models.IntegerField(default=0)

    max_passengers = models.IntegerField(default=3)
    current_passengers = models.IntegerField(default=0)

    completed = models.BooleanField(default=False)

    def current_node(self):
        if self.route and self.current_index < len(self.route):
            return self.route[self.current_index]
        return None
