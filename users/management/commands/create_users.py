from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


fake = Faker()


class Command(BaseCommand):
    """Creates mock user records in the database.

    Options:
        --help: Show help message and exit.

    Usage:
        $ python manage.py generate_mock_users 5
    """

    help = "Generates a specified amount of mock users"  # NOQA

    def add_arguments(self, parser) -> None:
        """Adds command-line arguments to the parser

        Args:
            parser(argparse.ArgumentParser): The argument parser
            to add arguments to
        """
        parser.add_argument(
            "users_num",
            type=int,
            choices=[number for number in range(1, 11)],
            help="The amount of users to create",
        )

    def handle(self, *args, **options) -> None:
        """Generates a specified amount of mock user records
        and saves them in the database. Each user is created
        with a random username, email, and password.

        Args:
            *args: additional positional arguments
            **options: Additional keyword arguments
                       containing the command options.

        """
        users = User.objects.bulk_create(
            [
                User(
                    username=fake.user_name(),
                    email=fake.email(),
                    password=make_password(
                        fake.password(
                            length=20,
                            special_chars=True,
                            digits=True,
                            upper_case=True,
                            lower_case=True,
                        )
                    ),
                )
                for _ in range(options["users_num"])
            ]
        )

        for user in users:
            user.save()
