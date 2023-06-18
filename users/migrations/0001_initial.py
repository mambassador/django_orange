# Generated by Django 4.2.2 on 2023-06-17 13:56

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=30)),
            ],
            managers=[
                ("users", django.db.models.manager.Manager()),
            ],
        ),
    ]
