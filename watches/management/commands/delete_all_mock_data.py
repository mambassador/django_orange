from django.core.management.base import BaseCommand

from watches.models import Brand, Designer, Store, Watch


class Command(BaseCommand):
    help = "Deletes all mock data from the tables"  # NOQA A003

    def handle(self, *args, **options):
        self.stdout.write("Deleting mock data...")

        Designer.objects.all().delete()
        Brand.objects.all().delete()
        Watch.objects.all().delete()
        Store.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Mock data deleted successfully."))
