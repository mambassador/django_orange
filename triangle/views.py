from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonModelForm, TriangleForm
from .models import Person


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


def create_person(request: HttpRequest) -> HttpResponse:
    """Creates a new person

    Args:
        request(HttpRequest): the HTTP request object

    Returns:
        response(HttpResponse): the HTTP response
    """
    if request.method == "POST":
        form = PersonModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("registered")

    else:
        form = PersonModelForm()

    response = render(request, "create_person_form.html", {"form": form})
    return response


def update_person(request: HttpRequest, pk) -> HttpResponse:
    """Updates a person

    Args:
        request(HttpRequest): the HTTP request object
        pk(int): the ID of the person to update

    Returns:
        response(HttpResponse): the HTTP response
    """
    person = get_object_or_404(Person, id=pk)

    if request.method == "POST":
        form = PersonModelForm(request.POST, instance=person)

        if form.is_valid():
            form.save()
            return redirect("edited")

    else:
        form = PersonModelForm(instance=person)

    response = render(request, "update_person.html", {"form": form, "person": person})
    return response


def registered(request: HttpRequest) -> HttpResponse:
    """Renders the informational successful registration page

    Args:
        request(HttpRequest): the HTTP request object

    Returns:
        response(HttpResponse): the HTTP response
    """
    response = render(request, "registered.html")
    return response


def edited(request: HttpRequest) -> HttpResponse:
    """Renders the informational successful person updating page

    Args:
        request(HttpRequest): the HTTP request object

    Returns:
        response(HttpResponse): the HTTP response
    """
    response = render(request, "edited.html")
    return response
