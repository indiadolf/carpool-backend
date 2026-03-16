from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Trip
from .serializers import TripSerializer
from .services import move_driver


@api_view(["POST"])
def create_trip(request):

    serializer = TripSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(["POST"])
def move_trip(request, trip_id):

    trip = Trip.objects.get(id=trip_id)

    trip = move_driver(trip)

    if trip.completed:
        return Response({"status": "trip completed"})

    return Response({
        "status": "driver moved",
        "current_node": trip.current_node.name,
        "route_index": trip.route_index
    })
@api_view(["GET"])
def driver_locations(request):

    trips = Trip.objects.filter(completed=False)

    data = []

    for trip in trips:
        data.append({
            "trip_id": trip.id,
            "node": trip.current_node.name
        })

    return Response(data)
@api_view(["GET"])
def analytics(request):

    from .models import Trip
    from carpool.models import Ride
    from payments.models import Transaction

    active_trips = Trip.objects.filter(completed=False).count()

    completed_trips = Trip.objects.filter(completed=True).count()

    passengers = Ride.objects.count()

    revenue = sum(t.amount for t in Transaction.objects.all())

    return Response({
        "active_trips": active_trips,
        "completed_trips": completed_trips,
        "passengers": passengers,
        "revenue": revenue
    })