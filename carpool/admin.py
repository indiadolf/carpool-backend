from django.contrib import admin
from .models import CarpoolRequest, Offer, Ride

admin.site.register(CarpoolRequest)
admin.site.register(Offer)
admin.site.register(Ride)