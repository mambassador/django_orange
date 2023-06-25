from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import TriangleForm


def calculate_hypotenuse(request: HttpRequest) -> HttpResponse:
    """Calculates the hypotenuse of a triangle based
    on the provided catheti values.

    Args:
        request(HttpRequest): The HTTP request object

    Returns:
        response(HttpResponse): The rendered HTML response containing
                                the form and calculated hypotenuse
    """
    hypotenuse = None
    form = TriangleForm()

    if request.GET:
        form = TriangleForm(request.GET)

        if form.is_valid():
            cathetus_1 = form.cleaned_data["cathetus_1"]
            cathetus_2 = form.cleaned_data["cathetus_2"]
            hypotenuse = (cathetus_1**2 + cathetus_2**2) ** 0.5

    response = render(request, "calc_hypo_form.html", {"form": form, "hypotenuse": hypotenuse})

    return response
