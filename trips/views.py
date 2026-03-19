from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Trip
from users.models import User
from network.models import Node



@api_view(["POST"])
def create_trip(request):
    try:
        driver = User.objects.get(id=request.data.get("driver"))
        start = Node.objects.get(id=request.data.get("start_node"))
        end = Node.objects.get(id=request.data.get("end_node"))

        
        route = [start.id, end.id]

        trip = Trip.objects.create(
            driver=driver,
            start_node=start,
            end_node=end,
            route=route,
            current_index=0,
            max_passengers=request.data.get("max_passengers", 3),
            current_passengers=0,
            completed=False
        )

        return Response({
            "status": "trip_created",
            "trip_id": trip.id,
            "route": route
        })

    except Exception as e:
        return Response({"error": str(e)})



@api_view(["POST"])
def update_location(request, trip_id):
    try:
        trip = Trip.objects.get(id=trip_id)

        if trip.current_index < len(trip.route) - 1:
            trip.current_index += 1
            trip.save()

        return Response({
            "status": "updated",
            "current_node": trip.route[trip.current_index],
            "current_index": trip.current_index
        })

    except Exception as e:
        return Response({"error": str(e)})



@api_view(["GET"])
def get_trips(request):

    trips = Trip.objects.all().values()

    return Response(list(trips))



@api_view(["POST"])
def cancel_trip(request, trip_id):

    try:
        trip = Trip.objects.get(id=trip_id)
    except Trip.DoesNotExist:
        return Response({"error": "Trip not found"})

    trip.completed = True
    trip.save()

    return Response({"status": "trip_cancelled"})



@api_view(["GET"])
def get_trip(request, trip_id):

    try:
        trip = Trip.objects.get(id=trip_id)
    except Trip.DoesNotExist:
        return Response({"error": "Trip not found"})

    return Response({
        "id": trip.id,
        "driver": trip.driver_id,
        "route": trip.route,
        "current_index": trip.current_index,
        "current_node": trip.current_node(),
        "max_passengers": trip.max_passengers,
        "current_passengers": trip.current_passengers,
        "completed": trip.completed
    })
