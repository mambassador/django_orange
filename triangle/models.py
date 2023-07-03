from django.db import models


class Person(models.Model):
    """Represents a person

    Attributes:
        first_name (str): The first name of the person
        last_name (str): The last name of the person
        email (str): The email address of the person
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(name="E-mail", unique=True)

    def __str__(self):
        """Returns a string representation of the person

        Returns:
            peron_str(str): the string representation of the person
        """
        person_str = self.first_name, self.last_name
        return person_str


METHOD_CHOICES = [
    ("GET", "GET"),
    ("POST", "POST"),
]


class Log(models.Model):
    """Represents a log for tracking requests

    Attributes:
        path (str): The path of the requested URL
        method (str): The HTTP method used for the request
        timestamp (datetime): The date and time when the log entry was created
        request_data (dict): The data transmitted with the request
        status_code (int): The HTTP status code of the response
        user (str): The username associated with the request
    """

    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    request_data = models.JSONField(blank=True, null=True)
    status_code = models.IntegerField()
    user = models.CharField(max_length=255)

    def __str__(self):
        """Returns string representation of the log model"""
        return f"{self.method}: {self.path}"
