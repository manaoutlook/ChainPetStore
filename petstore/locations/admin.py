from django.contrib import admin
from .models import Store, Warehouse

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'store_code', 'manager', 'phone')
    search_fields = ('name', 'store_code', 'address')
    list_filter = ('city', 'state')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'warehouse_code', 'capacity')
    search_fields = ('name', 'warehouse_code')
    list_filter = ('capacity',)
