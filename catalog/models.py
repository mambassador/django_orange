from django.db import models
from django.utils.timezone import now


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    products = models.ManyToManyField("Product")
    date_created = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
