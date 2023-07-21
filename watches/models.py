from django.db import models


class Designer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Watch(models.Model):
    name = models.CharField(max_length=100, unique=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    colour = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        verbose_name_plural = "Watches"

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100)
    watches = models.ManyToManyField(Watch)

    def __str__(self):
        return self.name
