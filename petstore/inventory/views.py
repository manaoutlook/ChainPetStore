from django.views.generic import TemplateView
from .models import Stock, InventoryMovement
from django.db.models import Sum

class InventoryDashboardView(TemplateView):
    template_name = 'inventory/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inventory Dashboard'
        
        # Get total stock quantities per product
        context['stock_summary'] = (
            Stock.objects.values('product__name')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('product__name')
        )
        
        # Get recent inventory movements
        context['recent_movements'] = (
            InventoryMovement.objects
            .select_related('product', 'from_location', 'to_location')
            .order_by('-movement_date')[:10]
        )
        
        return context
