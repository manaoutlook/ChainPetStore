from django.db import models
from products.models import Product
from locations.models import Store, Warehouse

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} at {self.store.name}"

class InventoryMovement(models.Model):
    MOVEMENT_TYPES = [
        ('STORE_TO_STORE', 'Store to Store'),
        ('STORE_TO_WAREHOUSE', 'Store to Warehouse'),
        ('WAREHOUSE_TO_STORE', 'Warehouse to Store'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_location = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='outgoing_movements')
    to_location = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='incoming_movements')
    quantity = models.PositiveIntegerField()
    movement_date = models.DateTimeField(auto_now_add=True)
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)

    def __str__(self):
        return f"{self.product.name} from {self.from_location.name} to {self.to_location.name}"
