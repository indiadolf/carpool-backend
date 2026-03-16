from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from .models import Node, Edge


@api_view(["GET"])
def network_graph(request):

    nodes = Node.objects.all()
    edges = Edge.objects.all()

    node_data = [
        {"data": {"id": node.name, "label": node.name}}
        for node in nodes
    ]

    edge_data = [
        {
            "data": {
                "source": edge.start_node.name,
                "target": edge.end_node.name
            }
        }
        for edge in edges
    ]

    return Response(node_data + edge_data)


def network_page(request):

    return render(request, "network.html")


def dashboard(request):

    return render(request, "dashboard.html")