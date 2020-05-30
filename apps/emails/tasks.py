import string
from gamein_backend.settings import EMAIL_HOST_USER

from celery import Task
from django.core.mail import EmailMessage


class SendEmailTask(Task):
    name = 'send_email'

    def run(self):
        return self.send_email()

    def send_email(self, email_message, subject: string, to: list):
        EmailMessage(subject, email_message, EMAIL_HOST_USER, to).send()
