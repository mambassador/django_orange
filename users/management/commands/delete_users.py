from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """A management command that deletes users specified by their IDs.
    Checks if the users exist and if they have superuser privileges before
    deleting them

    Options:
        --help: Show help message and exit.

    Usage:
        $ python manage.py delete_users 1 2 3
    """

    help = "Deletes users specified by their ids"  # NOQA

    def add_arguments(self, parser) -> None:
        """Adds command-line arguments to the parser.
        Multiple IDs can be provided, separated by spaces

        Args:
            parser(argparse.ArgumentParser): The argument parser
                                             to add arguments to
        """
        parser.add_argument(
            "user_ids",
            nargs="+",
            type=int,
            help="Ids of users to delete",
        )

    def handle(self, *args, **options) -> None:
        """Handles the command execution.
        Performs the deletion of users based on those IDs.
        Checks if the users exist and if they have superuser
        privileges before deleting them

        Args:
            *args: Additional positional arguments
            **options: Additional keyword arguments
                       containing the command options.

        Options:
            user_ids (list of int): IDs of users to delete.

        Raises:
            CommandError: If any of the specified user IDs are not
                          found or if superuser IDs are present in options
        """
        user_ids = options["user_ids"]

        if not any(User.objects.filter(id__in=user_ids, is_superuser=True)):
            if User.objects.filter(id__in=user_ids).count() == len(user_ids):
                User.objects.filter(id__in=user_ids).delete()

            else:
                raise CommandError("Some IDs were not found. The operation has been canceled.")
        else:
            raise CommandError("The operation has been canceled.")
