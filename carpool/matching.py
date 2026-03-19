from trips.models import Trip
from .models import Offer


def match_request(request):

    offers = []

    trips = Trip.objects.filter(completed=False)

    for trip in trips:

        # capacity check
        if trip.current_passengers >= trip.max_passengers:
            continue

        # route must contain pickup & drop
        if request.pickup_node_id not in trip.route:
            continue

        if request.drop_node_id not in trip.route:
            continue

        # pickup must be ahead of driver
        pickup_index = trip.route.index(request.pickup_node_id)

        if pickup_index < trip.current_index:
            continue

        # detour = distance from current position
        detour = pickup_index - trip.current_index

        # simple fare logic
        fare = 50 + detour * 10

        offer = Offer.objects.create(
            trip=trip,
            request=request,
            detour=detour,
            fare=fare
        )

        offers.append(offer)

    return offers