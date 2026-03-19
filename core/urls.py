from django.contrib import admin
from django.urls import path
from carpool.views import create_request, get_offers, accept_offer_api, cancel_ride, rate_ride
from trips.views import create_trip

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔥 YOUR APIs
    path('create_trip/', create_trip),
    path('create_request/', create_request),
    path('offers/', get_offers),
    path('accept_offer/<int:offer_id>/', accept_offer_api),
    path('cancel_ride/<int:ride_id>/', cancel_ride),
    path('rate_ride/<int:ride_id>/', rate_ride),
]