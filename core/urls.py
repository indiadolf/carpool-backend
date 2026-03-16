from django.contrib import admin
from django.urls import path

from trips.views import create_trip, move_trip
from carpool.views import create_request, get_offers, accept_offer_api
from network.views import network_graph, network_page
from trips.views import driver_locations 
from trips.views import analytics
from network.views import dashboard


urlpatterns = [

    path("admin/", admin.site.urls),
    path("drivers/", driver_locations),
    path("analytics/", analytics),
    path("dashboard/", dashboard),

    # Trip APIs
    path("create_trip/", create_trip),
    path("trip/<int:trip_id>/move/", move_trip),

    # Carpool APIs
    path("create_request/", create_request),
    path("offers/", get_offers),
    path("accept_offer/<int:offer_id>/", accept_offer_api),

    # Network visualization
    path("network/", network_graph),
    path("graph/", network_page),

]