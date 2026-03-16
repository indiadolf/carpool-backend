from .models import Trip
from .services import move_driver


def simulate_trips():

    trips = Trip.objects.filter(completed=False)

    for trip in trips:
        move_driver(trip)

        print(f"Trip {trip.id} moved to {trip.current_node}")