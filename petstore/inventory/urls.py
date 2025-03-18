from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.InventoryListView.as_view(), name='inventory-list'),
    path('create/', views.InventoryCreateView.as_view(), name='inventory-create'),
    path('<int:pk>/update/', views.InventoryUpdateView.as_view(), name='inventory-update'),
    path('<int:pk>/delete/', views.InventoryDeleteView.as_view(), name='inventory-delete'),
    path('<int:pk>/', views.InventoryDetailView.as_view(), name='inventory-detail'),
    path('dashboard/', views.InventoryDashboardView.as_view(), name='dashboard'),
]
