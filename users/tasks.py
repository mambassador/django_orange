from celery import shared_task

from core import settings

from django.core.mail import send_mail


@shared_task
def send_notification_mail(to_email, message, subject="Reminder") -> None:
    """Sends a notification email.

    Args:
        subject(str): the message subject
        to_email(List[str]): list of recipient email addresses
        message(str): the message content
    """
    send_mail(
        subject,
        message,
        settings.NOREPLY_EMAIL,
        to_email,
        fail_silently=False,
    )
