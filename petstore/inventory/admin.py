from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'quantity')
    list_filter = ('location', 'product__category')
    search_fields = ('product__name', 'location__name')
    raw_id_fields = ('product', 'location')