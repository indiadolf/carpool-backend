from .models import Trip
from .services import move_driver


def simulate_trips():

    trips = Trip.objects.filter(completed=False)

    for trip in trips:

        trip = move_driver(trip)

        node_name = None
        if trip.current_node:
            node_name = trip.current_node.name

        print(f"Trip {trip.id} moved to {node_name}")