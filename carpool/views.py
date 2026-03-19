from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CarpoolRequest, Offer, Ride, Rating
from .serializers import OfferSerializer
from .services import accept_offer
from .matching import match_request


# ✅ CREATE REQUEST + MATCH
@api_view(["POST"])
def create_request(request):

    data = request.data

    carpool_request = CarpoolRequest.objects.create(
        passenger_id=data.get("passenger"),
        pickup_node_id=data.get("pickup_node"),
        drop_node_id=data.get("drop_node")
    )

    offers = match_request(carpool_request)

    return Response({
        "status": "request_created",
        "request_id": carpool_request.id,
        "offers_created": len(offers)
    })


# ✅ GET OFFERS
@api_view(["GET"])
def get_offers(request):

    request_id = request.GET.get("request_id")

    if not request_id:
        return Response({"error": "request_id required"})

    offers = Offer.objects.filter(request_id=request_id)

    serializer = OfferSerializer(offers, many=True)

    return Response(serializer.data)


# ✅ ACCEPT OFFER → CREATE RIDE
@api_view(["POST"])
def accept_offer_api(request, offer_id):

    try:
        offer = Offer.objects.get(id=offer_id)
    except Offer.DoesNotExist:
        return Response({"error": "Offer not found"})

    ride = accept_offer(offer)

    if not ride:
        return Response({"error": "Could not accept offer"})

    return Response({
        "status": "accepted",
        "ride_id": ride.id
    })


# ✅ CANCEL RIDE
@api_view(["POST"])
def cancel_ride(request, ride_id):

    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found"})

    trip = ride.trip

    if trip.current_passengers > 0:
        trip.current_passengers -= 1
        trip.save()

    ride.delete()

    return Response({"status": "cancelled"})


# ✅ RATE RIDE
@api_view(["POST"])
def rate_ride(request, ride_id):

    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found"})

    Rating.objects.create(
        ride=ride,
        passenger=ride.passenger,
        driver=ride.trip.driver,
        score=request.data.get("score"),
        comment=request.data.get("comment", "")
    )

    return Response({"status": "rated"})


# ✅ DRIVER VIEW (PS REQUIREMENT)
@api_view(["GET"])
def driver_requests(request, trip_id):

    offers = Offer.objects.filter(trip_id=trip_id)

    serializer = OfferSerializer(offers, many=True)

    return Response(serializer.data)