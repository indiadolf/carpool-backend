from .models import Trip
from network.models import Node
from routing.utils import shortest_path


def initialize_trip_route(trip):

    try:
        start = trip.start_node
        end = trip.end_node

        route = shortest_path(start, end)

        if route:
            trip.route = route
            trip.route_index = 0

            # set current node
            trip.current_node = start

            trip.save()

    except Exception:
        pass

    return trip


def move_driver(trip):

    if not trip.route or trip.completed:
        return trip

    # reached end
    if trip.route_index >= len(trip.route) - 1:
        trip.completed = True
        trip.save()
        return trip

    # move forward
    trip.route_index += 1

    next_node_name = trip.route[trip.route_index]

    try:
        node = Node.objects.get(name=next_node_name)
        trip.current_node = node
    except Node.DoesNotExist:
        pass

    # mark started
    if trip.route_index > 0:
        trip.started = True

    trip.save()

    return trip