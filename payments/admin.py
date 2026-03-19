from django.contrib import admin
from .models import Wallet, Transaction


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "balance")

    search_fields = ("user__username",)

    list_filter = ("balance",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "wallet",
        "user",
        "amount",
        "type",
        "created_at"
    )

    list_filter = ("type", "created_at")

    search_fields = ("wallet__user__username",)

    def user(self, obj):
        return obj.wallet.user.username