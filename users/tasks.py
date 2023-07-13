from celery import shared_task
from django.core.mail import send_mail

from core import settings


@shared_task
def send_notification_mail(to_email, message) -> None:
    """Sends a notification email.

    Args:
        to_email: (List[str]): list of recipient email addresses
        message: the message content
    """
    send_mail(
        "Notification",
        message,
        settings.NOREPLY_EMAIL,
        to_email,
        fail_silently=False,
    )
