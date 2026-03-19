from django.contrib import admin
from .models import Node, Edge


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ["id", "from_node", "to_node"]
    list_filter = ["from_node", "to_node"]