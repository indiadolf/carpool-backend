from django.db import models
from users.models import User


class Wallet(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.FloatField(default=100)

    def __str__(self):
        return f"{self.user.username} wallet"


class Transaction(models.Model):

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    amount = models.FloatField()

    type = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.user.username} {self.amount}"