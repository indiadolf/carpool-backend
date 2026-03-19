from rest_framework import serializers
from .models import CarpoolRequest, Offer


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarpoolRequest
        fields = [
            "id",
            "passenger",
            "pickup_node",
            "drop_node",
            "created_at"
        ]


class OfferSerializer(serializers.ModelSerializer):

    driver = serializers.CharField(source="trip.driver.username", read_only=True)

    class Meta:
        model = Offer
        fields = [
            "id",
            "driver",
            "trip",
            "request",
            "detour",
            "fare",
            "accepted"
        ]