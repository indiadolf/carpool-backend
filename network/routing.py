from django.urls import path
from .consumers import GraphConsumer

websocket_urlpatterns = [
    path("ws/graph/", GraphConsumer.as_asgi()),
]