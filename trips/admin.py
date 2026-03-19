from django.apps import AppConfig
from django.contrib import admin
from .models import Trip

admin.site.register(Trip)

class TripsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trips'