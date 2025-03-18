from django.db import models
from products.models import Product
from locations.models import Location

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} at {self.location.name}"

    class Meta:
        unique_together = ('product', 'location')
