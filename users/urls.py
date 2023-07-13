from django.urls import path

from .views import create_notification


app_name = "users"

urlpatterns = [
    path("", create_notification, name="email-notification"),
]
