from random import sample

from django.core.management.base import BaseCommand

from faker import Faker

from watches.models import Brand, Designer, Store, Watch


class Command(BaseCommand):
    help = "Generates mock data for watches app"  # NOQA A003

    def handle(self, *args, **options) -> None:
        """
        Creates:
            Mock designers: 500 instances
            Mock brands: 1000 instances
            Mock watches: 3000 instances
            Mock stores: 10 instances, each associated with 150 random watches

        Notes:
            - The command assumes that the necessary models (Designer, Brand, Store, Watch)
              are defined in the 'watches' app.
            - Faker library is used to generate realistic mock data.
            - The generated data includes names, prices, colours, sizes,
              and associations between models.

        Usage:
            python manage.py generate_mock_data
        """
        fake = Faker()

        self.stdout.write("Creating mock designers...")
        designers = []
        for _ in range(500):
            designer = Designer(name=fake.name())
            designers.append(designer)
        Designer.objects.bulk_create(designers)
        self.stdout.write(self.style.SUCCESS("Mock designers created successfully."))

        self.stdout.write("Creating mock brands...")
        brands = []
        for _ in range(1000):
            brand = Brand(name=fake.company(), country=fake.country())
            brands.append(brand)
        Brand.objects.bulk_create(brands)
        self.stdout.write(self.style.SUCCESS("Mock brands created successfully."))

        self.stdout.write("Creating mock watches...")
        watches = []
        designers = list(Designer.objects.all())
        brands = list(Brand.objects.all())

        for _ in range(20000):
            if fake.boolean(chance_of_getting_true=50):
                watch = Watch(
                    name=" ".join([fake.word().title() for _ in range(2)]),
                    price=fake.pydecimal(min_value=10, max_value=1000, right_digits=2),
                    colour=fake.safe_color_name().title(),
                    size=fake.pydecimal(min_value=20, max_value=50, right_digits=1),
                    designer=fake.random_element(designers),
                    brand=fake.random_element(brands),
                )
            else:
                watch = Watch(
                    name=fake.word().title(),
                    price=fake.pydecimal(min_value=10, max_value=1000, right_digits=2),
                    colour=fake.safe_color_name().title(),
                    size=fake.pydecimal(min_value=20, max_value=50, right_digits=1),
                    designer=fake.random_element(designers),
                    brand=fake.random_element(brands),
                )
            watches.append(watch)

        Watch.objects.bulk_create(watches)
        self.stdout.write(self.style.SUCCESS("Fake watches created successfully."))

        self.stdout.write("Creating mock stores...")
        stores = []
        for _ in range(50):
            store = Store(name=fake.company())
            store.save()
            stores.append(store)
            for store in stores:
                store_watches = sample(watches, 300)
                store.watches.set(store_watches)
                self.stdout.write(f"Created store {_} {store.name}")

        self.stdout.write(self.style.SUCCESS("Mock stores created successfully."))

        self.stdout.write(self.style.SUCCESS("Mock data generation complete."))
