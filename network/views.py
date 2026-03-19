from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Node, Edge
from trips.models import Trip
from carpool.models import CarpoolRequest, Offer
from users.models import User

import json


# ===================== 🌐 NETWORK GRAPH =====================

@api_view(["GET"])
def network_graph(request):

    nodes = Node.objects.all()
    edges = Edge.objects.all()
    trips = Trip.objects.all()
    requests = CarpoolRequest.objects.all()

    demand = {}

    # 🔥 Demand calculation
    for r in requests:
        node = r.pickup_node.name
        demand[node] = demand.get(node, 0) + 1

    elements = []

    # ================= NODES =================
    for node in nodes:
        elements.append({
            "data": {
                "id": node.name,
                "label": node.name,
                "demand": demand.get(node.name, 0)
            }
        })

    # ================= EDGES =================
    for edge in edges:
        elements.append({
            "data": {
                "source": edge.start_node.name,
                "target": edge.end_node.name
            }
        })

    # ================= DRIVER + ROUTES =================
    for trip in trips:

        if not trip.route:
            continue

        route = trip.route
        current_index = trip.route_index

        # 🚗 Driver position
        if current_index < len(route):
            current_node = route[current_index]

            elements.append({
                "data": {
                    "id": f"driver_{trip.id}",
                    "label": "🚗",
                    "node": current_node
                },
                "classes": "driver"
            })

        # ================= ROUTE OPTIMIZATION =================
        # 🔥 highlight only remaining route (optimization)
        optimized_route = route[current_index:]

        for i in range(len(optimized_route) - 1):
            elements.append({
                "data": {
                    "source": optimized_route[i],
                    "target": optimized_route[i + 1]
                },
                "classes": "route"
            })

    # ================= PASSENGERS =================
    for r in requests:
        elements.append({
            "data": {
                "id": f"pickup_{r.id}",
                "label": "🧍",
                "node": r.pickup_node.name
            },
            "classes": "pickup"
        })

    return Response(elements)


# ===================== PAGE =====================

def network_page(request):
    return render(request, "network.html")


# ===================== DRIVER POSITIONS =====================

@api_view(["GET"])
def driver_positions(request):

    trips = Trip.objects.all()
    drivers = []

    for trip in trips:
        if trip.route and trip.route_index < len(trip.route):

            drivers.append({
                "driver": trip.driver.username,
                "node": trip.route[trip.route_index],
                "remaining_route": trip.route[trip.route_index:]
            })

    return Response(drivers)


# ===================== 📍 DRIVER LOCATION =====================

@csrf_exempt
def update_location(request):

    if request.method == "POST":
        data = json.loads(request.body)

        driver = User.objects.get(id=data["driver_id"])

        driver.lat = data["lat"]
        driver.lng = data["lng"]
        driver.save()

        return JsonResponse({"status": "updated"})

    return JsonResponse({"error": "invalid request"})


def get_driver_location(request):

    driver = User.objects.filter(role="driver").first()

    if not driver or driver.lat is None:
        return JsonResponse({"error": "no driver"})

    return JsonResponse({
        "lat": driver.lat,
        "lng": driver.lng
    })