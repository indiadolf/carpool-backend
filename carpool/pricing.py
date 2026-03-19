from trips.models import Trip
from .models import CarpoolRequest

BASE_FARE = 10
PRICE_PER_NODE = 2


def get_surge_multiplier():

    active_requests = CarpoolRequest.objects.count()

    
    active_trips = Trip.objects.filter(active=True).count()

  
    if active_trips == 0:
        return 2

    ratio = active_requests / max(active_trips, 1)

   
    if ratio < 1:
        return 1

    elif ratio < 2:
        return 1.25

    elif ratio < 3:
        return 1.5

    else:
        return 2


def calculate_fare(distance, passengers):

    surge = get_surge_multiplier()

    base_price = BASE_FARE + distance * PRICE_PER_NODE

    price = base_price * surge

    # safety
    passengers = max(passengers, 1)

    # split fare
    price = price / passengers

    return round(price, 2)
