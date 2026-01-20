from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    avatar = models.ImageField(upload_to='users/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

class CarModel(models.Model):

    brand = models.CharField("Марка", max_length=100)
    name = models.CharField("Модель", max_length=100)
    vin_prefix = models.CharField("Первые 9 знаков VIN", max_length=9, unique=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

class Part(models.Model):

    name = models.CharField("Название", max_length=255)
    oem_code = models.CharField("OEM Артикул", max_length=50, db_index=True)
    category = models.CharField("Категория", max_length=100)
    price = models.DecimalField("Цена (₽)", max_digits=10, decimal_places=2)

    compatible_with = models.ManyToManyField(CarModel, related_name='parts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.oem_code} - {self.name}"