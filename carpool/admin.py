from django.contrib import admin
from .models import CarpoolRequest, Offer, Ride, Rating


@admin.register(CarpoolRequest)
class CarpoolRequestAdmin(admin.ModelAdmin):

    list_display = ("id", "passenger", "pickup_node", "drop_node", "created_at")
    search_fields = ("passenger__username",)
    list_filter = ("created_at",)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):

    list_display = ("id", "trip", "request", "detour", "fare", "accepted")
    list_filter = ("accepted", "trip")
    search_fields = ("request__passenger__username",)


@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):

    list_display = ("id", "trip", "passenger", "pickup_node", "drop_node", "fare")
    search_fields = ("passenger__username",)
    list_filter = ("trip",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ("id", "ride", "driver", "score")
    search_fields = ("driver__username",)
    list_filter = ("score",)