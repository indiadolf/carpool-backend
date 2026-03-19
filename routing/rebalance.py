from trips.models import Trip
from carpool.models import CarpoolRequest
from network.models import Node
from routing.utils import shortest_path


def rebalance_drivers():

    requests = CarpoolRequest.objects.all()

    if not requests:
        return


    demand = {}

    for r in requests:
        node = r.pickup_node.name
        demand[node] = demand.get(node, 0) + 1


    target_name = max(demand, key=demand.get)

    try:
        target_node = Node.objects.get(name=target_name)
    except Node.DoesNotExist:
        return

    trips = Trip.objects.all()

    for trip in trips:

        if not trip.route:
            continue

        current_node_name = trip.route[trip.route_index]

        try:
            start_node = Node.objects.get(name=current_node_name)
        except Node.DoesNotExist:
            continue

        new_route = shortest_path(start_node, target_node)

        if new_route and len(new_route) > 1:

            trip.route = new_route
            trip.route_index = 0
            trip.save()
