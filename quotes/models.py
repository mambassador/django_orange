from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=70)
    date_of_birth = models.DateField
    city_of_birth = models.CharField(max_length=70, blank=True)
    country_of_birth = models.CharField(max_length=70)
    description = models.TextField()

    def __str__(self):
        return self.full_name


class Quote(models.Model):
    text = models.CharField(max_length=1000, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
