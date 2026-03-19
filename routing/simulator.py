from trips.models import Trip


def move_drivers():

    trips = Trip.objects.all()

    for trip in trips:

        if not trip.route:
            continue

        if trip.route_index < len(trip.route) - 1:
            trip.route_index += 1
        else:
         
            trip.route_index = len(trip.route) - 1

        trip.save()
