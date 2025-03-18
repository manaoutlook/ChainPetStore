from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from .models import Inventory
from django.db.models import Sum

class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventories'
    paginate_by = 10

class InventoryCreateView(CreateView):
    model = Inventory
    template_name = 'inventory/inventory_form.html'
    fields = ['product', 'location', 'quantity']
    success_url = reverse_lazy('inventory:inventory-list')

class InventoryUpdateView(UpdateView):
    model = Inventory
    template_name = 'inventory/inventory_form.html'
    fields = ['product', 'location', 'quantity']
    success_url = reverse_lazy('inventory:inventory-list')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:inventory-list')

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'inventory'

class InventoryDashboardView(TemplateView):
    template_name = 'inventory/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inventory Dashboard'
        
        # Get total inventory quantities per product
        context['inventory_summary'] = (
            Inventory.objects.values('product__name')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('product__name')
        )
        
        # Get inventory distribution across locations
        context['location_distribution'] = (
            Inventory.objects.values('location__name', 'product__name')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('location__name', 'product__name')
        )
        
        return context
