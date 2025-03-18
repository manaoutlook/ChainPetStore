from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include(('products.urls', 'products'))),
    path('locations/', include('locations.urls')),
    path('inventory/', include(('inventory.urls', 'inventory'))),
]
