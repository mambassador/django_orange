from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.utils import timezone

from .forms import EmailNotificationForm
from .tasks import send_notification_mail


def create_notification(request):
    """Creates a time-delayed e-mail notification. Uses Celery
    to perform delayed task and time from user input

    The time specified by user is passed to the "eta" argument
    of the function send_notification_mail.apply_async()
    """
    if request.method == "POST":
        form = EmailNotificationForm(request.POST)

        if form.is_valid():
            send_notification_mail.apply_async(
                kwargs={"to_email": [form.cleaned_data["to_email"]], "message": form.cleaned_data["message"]},
                eta=form.cleaned_data["send_time"],
            )

            return HttpResponseRedirect(reverse("watches:index"))

    else:
        initial_data = {
            "send_time": timezone.now(),
        }
        form = EmailNotificationForm(initial=initial_data)

    return render(request, "users/email-notification.html", {"form": form})
