from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CarpoolRequest, Offer
from .serializers import RequestSerializer, OfferSerializer

from .services import accept_offer


@api_view(["POST"])
def create_request(request):

    serializer = RequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(["GET"])
def get_offers(request):

    offers = Offer.objects.all()

    serializer = OfferSerializer(offers, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def accept_offer_api(request, offer_id):

    offer = Offer.objects.get(id=offer_id)

    ride = accept_offer(offer)

    return Response({"status": "accepted"})