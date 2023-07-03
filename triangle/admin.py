from django.contrib import admin

from .models import Log, Person


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    """Admin interface configuration for the Log model"""

    list_display = (
        "path",
        "method",
        "status_code",
        "user",
        "timestamp",
        "request_data",
    )
    search_fields = ("path",)
    list_filter = ("timestamp", "method", "status_code")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Admin interface configuration for the Person model"""

    list_display = ("id", "first_name", "last_name", "E-mail")
