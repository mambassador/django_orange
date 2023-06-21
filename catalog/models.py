from django.db import models
from django.utils.timezone import now


class City(models.Model):
    """Represents a city

    Attributes:
        name (CharField): the name of the city
        country (CharField): the country the city belongs to
    """

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self) -> models.CharField:
        """Returns a string representation of the city

        Returns:
            self.name (str): The name of the city
        """
        return self.name


class Customer(models.Model):
    """Represents a customer

    Attributes:
        first_name (CharField): The first name of the customer
        last_name (CharField): The last name of the customer
        city (ForeignKey): The city the customer belongs to (foreign key)
        products (ManyToManyField): The products purchased by the customer
        date_created (DateTimeField): The date and time the customer was created
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    products = models.ManyToManyField("Product")
    date_created = models.DateTimeField(default=now)

    def __str__(self) -> str:
        """Returns a string representation of the customer

        Returns:
            self.name (str): The name of the customer
        """
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    """Represents a product

    Attributes:
        name (CharField): The name of the product
        price (PositiveIntegerField): The price of the product
    """

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)

    def __str__(self) -> models.CharField:
        """Returns a string representation of the product

        Returns:
            self.name (str): The name of the customer
        """
        return self.name


class Supplier(models.Model):
    """Represents a supplier

    Attributes:
        name (CharField): The name of the supplier
        city (OneToOneField): The city the supplier is located in (one-to-one relationship)
    """

    name = models.CharField(max_length=50)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self) -> models.CharField:
        """Returns a string representation of the supplier

        Returns:
            self.name (str): The name of the supplier
        """
        return self.name
