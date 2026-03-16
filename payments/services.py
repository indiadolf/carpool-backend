from .models import Wallet, Transaction


def process_payment(passenger, driver, amount):

    passenger_wallet = Wallet.objects.get(user=passenger)

    driver_wallet = Wallet.objects.get(user=driver)

    if passenger_wallet.balance < amount:
        return False

    passenger_wallet.balance -= amount
    driver_wallet.balance += amount

    passenger_wallet.save()
    driver_wallet.save()

    Transaction.objects.create(
        sender=passenger,
        receiver=driver,
        amount=amount
    )

    return True