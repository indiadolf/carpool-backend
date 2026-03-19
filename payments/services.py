from django.db import transaction
from .models import Wallet, Transaction


def process_payment(passenger, driver, amount):

    try:
        with transaction.atomic():

            passenger_wallet = Wallet.objects.select_for_update().get(user=passenger)
            driver_wallet = Wallet.objects.select_for_update().get(user=driver)

            if passenger_wallet.balance < amount:
                return False

            passenger_wallet.balance -= amount
            driver_wallet.balance += amount

            passenger_wallet.save()
            driver_wallet.save()

            Transaction.objects.create(
                wallet=passenger_wallet,
                amount=-amount,
                type="ride_payment"
            )

            Transaction.objects.create(
                wallet=driver_wallet,
                amount=amount,
                type="ride_earning"
            )

            return True

    except Exception:
        return False