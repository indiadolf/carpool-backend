from rest_framework import serializers
from .models import CarpoolRequest, Offer


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarpoolRequest
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = "__all__"