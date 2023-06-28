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
