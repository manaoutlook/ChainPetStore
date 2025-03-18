from django.contrib import admin
from .models import Stock, InventoryMovement

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'quantity')
    list_filter = ('store', 'product__category')
    search_fields = ('product__name', 'store__name')
    raw_id_fields = ('product', 'store')

@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'from_location', 'to_location', 'quantity', 'movement_date')
    list_filter = ('movement_type', 'movement_date')
    search_fields = ('product__name', 'from_location__name', 'to_location__name')
    date_hierarchy = 'movement_date'
    raw_id_fields = ('product', 'from_location', 'to_location')
