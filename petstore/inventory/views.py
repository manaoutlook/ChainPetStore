from django.views.generic import TemplateView

class InventoryDashboardView(TemplateView):
    template_name = 'inventory/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add inventory data to context
        context['title'] = 'Inventory Dashboard'
        return context
