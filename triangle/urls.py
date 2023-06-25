from django.urls import path

from .views import calculate_hypotenuse


app_name = "triangle"

urlpatterns = [
    path("", calculate_hypotenuse, name="calc_hypo"),
]
