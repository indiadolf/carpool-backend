from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = [
            "id",
            "driver",
            "start_node",
            "end_node",
            "route",
            "max_passengers",
            "current_node"
        ]

        read_only_fields = [
            "id",
            "route_index",
            "current_passengers",
            "started",
            "completed",
            "created_at"
        ]