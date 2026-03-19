from django.db import transaction
from .models import Offer, Ride
from payments.services import process_payment


def accept_offer(offer):

 
    if offer.accepted:
        print("❌ Offer already accepted")
        return None

    trip = offer.trip


    if trip.current_passengers >= trip.max_passengers:
        print("❌ Trip full")
        return None

    passenger = offer.request.passenger
    driver = trip.driver

    try:
        with transaction.atomic():

         
            success = process_payment(passenger, driver, offer.fare)

            if not success:
                print("❌ Payment failed")
                return None

          
            trip.current_passengers += 1
            trip.save()

        
            ride = Ride.objects.create(
                trip=trip,
                passenger=passenger,
                pickup_node=offer.request.pickup_node,
                drop_node=offer.request.drop_node,
                fare=offer.fare
            )

    
            offer.accepted = True
            offer.save()

            print("✅ Ride created:", ride.id)

            return ride

    except Exception as e:
        print("❌ ERROR:", str(e))
        return None
