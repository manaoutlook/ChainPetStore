from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.InventoryDashboardView.as_view(), name='dashboard'),
    path('inventory/', views.InventoryListView.as_view(), name='inventory-list'),
    path('inventory/create/', views.InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/<int:pk>/', views.InventoryDetailView.as_view(), name='inventory-detail'),
    path('inventory/<int:pk>/update/', views.InventoryUpdateView.as_view(), name='inventory-update'),
    path('inventory/<int:pk>/delete/', views.InventoryDeleteView.as_view(), name='inventory-delete'),
]
