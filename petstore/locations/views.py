from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Location

class LocationListView(ListView):
    model = Location
    template_name = 'locations/location_list.html'
    context_object_name = 'locations'

class LocationDetailView(DetailView):
    model = Location
    template_name = 'locations/location_detail.html'
    context_object_name = 'location'

class LocationCreateView(CreateView):
    model = Location
    template_name = 'locations/location_form.html'
    fields = ['name', 'address', 'city', 'state', 'zip_code']
    success_url = reverse_lazy('locations:list')

class LocationUpdateView(UpdateView):
    model = Location
    template_name = 'locations/location_form.html'
    fields = ['name', 'address', 'city', 'state', 'zip_code']
    success_url = reverse_lazy('locations:list')

class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'locations/location_confirm_delete.html'
    success_url = reverse_lazy('locations:list')
