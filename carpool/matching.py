from trips.models import Trip
from .models import Offer
from routing.utils import shortest_path
from .pricing import calculate_fare


MAX_DETOUR = 3


def match_request(request):

    offers = []

    trips = Trip.objects.filter(completed=False)

    for trip in trips:

        route = trip.route

        pickup = request.pickup_node.name
        drop = request.drop_node.name

        # find nearest route node to pickup
        for node in route:

            try:
                pickup_path = shortest_path(node, pickup)

                drop_path = shortest_path(pickup, drop)

            except:
                continue

            if not pickup_path or not drop_path:
                continue

            detour = len(pickup_path) + len(drop_path)

            if detour > MAX_DETOUR:
                continue

            fare = calculate_fare(detour, trip.current_passengers + 1)

            offer = Offer.objects.create(
                trip=trip,
                request=request,
                detour=detour,
                fare=fare
            )

            offers.append(offer)

            break

    return offers