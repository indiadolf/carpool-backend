from trips.models import Trip


def move_drivers():

    trips = Trip.objects.all()

    for trip in trips:

        if trip.route_index < len(trip.route) - 1:

            trip.route_index += 1
            trip.save()