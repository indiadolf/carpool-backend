from .models import Offer, Ride


from payments.services import process_payment


def accept_offer(offer):

    trip = offer.trip

    if trip.current_passengers >= trip.max_passengers:
        return None

    passenger = offer.request.passenger
    driver = trip.driver

    success = process_payment(passenger, driver, offer.fare)

    if not success:
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

    return ride