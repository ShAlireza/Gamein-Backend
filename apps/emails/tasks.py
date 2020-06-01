import string

from celery.task import Task
from django.core.mail import EmailMultiAlternatives

from gamein_backend.settings import EMAIL_HOST_USER


class SendEmailTask(Task):
    name = 'send_email'

    def run(self, html_message: string, text_message: string, subject: string, to: list):
        return self.send_email(html_message, text_message, subject, to)

    def send_email(self, html_message: string, text_message: string, subject: string, to: list):
        mail = EmailMultiAlternatives(
            subject=subject,
            body=text_message,
            from_email=EMAIL_HOST_USER,
            to=to)
        mail.attach_alternative(html_message, "text/html")
        mail.send()
