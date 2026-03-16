from .models import Trip
from network.models import Node


def move_driver(trip):

    route = trip.route

    # Trip already finished
    if trip.completed:
        return None

    # End reached
    if trip.route_index >= len(route) - 1:
        trip.completed = True
        trip.save()
        return trip

    # Move forward
    trip.route_index += 1

    next_node_name = route[trip.route_index]

    node = Node.objects.get(name=next_node_name)

    trip.current_node = node

    # trip starts when first move happens
    if trip.route_index > 0:
        trip.started = True

    trip.save()

    return trip