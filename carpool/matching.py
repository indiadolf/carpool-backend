from trips.models import Trip
from .models import Offer


def match_request(request):

    offers = []

    trips = Trip.objects.filter(completed=False)

    for trip in trips:

    
        if trip.current_passengers >= trip.max_passengers:
            continue

       
        if request.pickup_node_id not in trip.route:
            continue

        if request.drop_node_id not in trip.route:
            continue


        pickup_index = trip.route.index(request.pickup_node_id)

        if pickup_index < trip.current_index:
            continue

      
        detour = pickup_index - trip.current_index


        fare = 50 + detour * 10

        offer = Offer.objects.create(
            trip=trip,
            request=request,
            detour=detour,
            fare=fare
        )

        offers.append(offer)

    return offers
