import string
from gamein_backend.settings import EMAIL_HOST_USER

from celery import Task
from django.core.mail import EmailMultiAlternatives


class SendEmailTask(Task):
    name = 'send_email'

    def run(self):
        return self.send_email()

    def send_email(self, text: string, subject: string, to: list):
        # TODO: set email content based on email template
        email_text_message = None  # TODO: render text to string
        email_html_message = None  # TODO: render html to string
        mail = EmailMultiAlternatives(
            subject=subject,
            body=email_text_message,
            from_email=EMAIL_HOST_USER,
            to=to)
        mail.attach_alternative(email_html_message, "text/html")
        mail.send()
