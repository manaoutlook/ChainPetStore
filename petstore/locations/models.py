from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"

    class Meta:
        ordering = ['name']

class Store(Location):
    store_code = models.CharField(max_length=10, unique=True)
    manager = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

class Warehouse(Location):
    warehouse_code = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
