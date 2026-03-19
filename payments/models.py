from django.db import models
from users.models import User


class Wallet(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return f"{self.user.username} wallet"


class Transaction(models.Model):

    TRANSACTION_TYPES = [
        ("ride_payment", "Ride Payment"),
        ("ride_earning", "Ride Earning"),
        ("wallet_topup", "Wallet Topup"),
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.user.username} {self.amount}"