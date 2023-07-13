from django import forms
from django.utils import timezone


class EmailNotificationForm(forms.Form):
    """Form for creating e-mail notification"""

    to_email = forms.EmailField(label="E-mail address",
                                widget=forms.EmailInput(attrs={"autocomplete": 'new-email',
                                                               "placeholder": "Enter e-mail"}))

    message = forms.CharField(max_length=1000,
                              label="Message",
                              widget=forms.TextInput(attrs={"autocomplete": "off" + "always",
                                                            "placeholder": "Enter the text"}))

    send_time = forms.DateTimeField(label="Send time",
                                    widget=forms.DateTimeInput(attrs={"autocomplete": "on"}))

    def clean_send_time(self):
        """Cleans and validates the send time

        Returns:
            send_time(datetime.datetime): Cleaned and validated send time.

        Raises:
            forms.ValidationError: If the send time is not within the allowed range.
        """
        now = timezone.now()
        send_time = self.cleaned_data.get("send_time")

        if send_time and (send_time < now or send_time > now + timezone.timedelta(days=2)):
            raise forms.ValidationError("Send time must be from now to 2 days in the future.")

        return send_time
