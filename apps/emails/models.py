from django.contrib.auth.models import User
from django.db import models
from django.template import Context, Template
from martor.models import MartorField
from apps.accounts.models import Profile

import string
import re


class EmailTemplate(models.Model):
    title = models.CharField(null=False, max_length=50)
    html = MartorField()
    text = models.TextField(null=False)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        fields = self.find_template_variables(self.html)
        for field in fields:
            EmailTemplateField.objects.create(field_name=field, template=self)

    def find_template_variables(self, template):
        fields = re.findall('{{\s(\w+)\s}}', template)
        return fields


class EmailTemplateField(models.Model):
    field_name = models.TextField()
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)


class Mail(models.Model):
    template = models.OneToOneField(to=EmailTemplate, on_delete=models.CASCADE)
    subject = models.CharField(blank=True, null=True, max_length=100)
    values_of_fields = models.TextField(blank=False, null=False)
    html_context = models.TextField()
    text_context = models.TextField()
    recipients = models.ManyToManyField(User)

    def __str__(self):
        return self.subject

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        context = dict()
        email_values = re.split('\s?\n?\$\$\s?\n?', self.values_of_fields)
        template_fields = self.template.emailtemplatefield_set.all().values_list('field_name', flat=True)
        for (field, value) in zip(template_fields, email_values):
            context[field] = value
        if not self.subject:
            self.subject = context.get('subject')
        self.set_values_to_template_fields(context)
        super().save(force_insert, force_update, using, update_fields)

    def set_values_to_template_fields(self, context):
        self.html_context = self.render_email_templates(self.template.html, context)
        self.text_context = self.render_email_templates(self.template.text, context)

    def render_email_templates(self, template: string, context: dict):
        return Template(template).render(Context(context))
