import string

from celery.task import Task
from django.conf.global_settings import EMAIL_HOST_USER
from django.template import Template, Context

from apps.emails.models import EmailTemplate

from django.core.mail import EmailMultiAlternatives


class SendEmailTask(Task):
    name = 'send_email'

    def run(self, template: EmailTemplate, content_text: string, subject: string, to: list):
        return self.send_email(template, content_text, subject, to)

    def send_email(self, template: EmailTemplate, content_text: string, subject: string, to: list):
        content = {
            'subject': subject,
            'context': content_text
        }
        email_text_message = self.render_email_templates(template.text, content)
        email_html_message = self.render_email_templates(template.html, content)
        mail = EmailMultiAlternatives(
            subject=subject,
            body=email_text_message,
            from_email=EMAIL_HOST_USER,
            to=to)
        mail.attach_alternative(email_html_message, "text/html")
        mail.send()

    def render_email_templates(self, template: string, context: dict):
        return Template(template).render(Context(context))
