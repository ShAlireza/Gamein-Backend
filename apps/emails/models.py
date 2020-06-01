from django.db import models
from martor.models import MartorField
from rest_framework.fields import ListField, DictField

import re

from apps.accounts.models import Profile


class EmailTemplate(models.Model):
    title = models.CharField(null=False, max_length=50)
    html = MartorField()
    text = models.TextField(null=False)
    fields = ListField()

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.fields = self.find_template_variables(self)
        super().save(force_insert, force_update, using, update_fields)

    def find_template_variables(self, template):
        fields = re.findall('{{\s(\w+)\s}}', template.html)
        return fields


class Email(models.Model):
    template = models.OneToOneField(to=EmailTemplate, on_delete=models.CASCADE)
    subject = models.CharField(null=False, max_length=100)
    content = models.TextField(null=False)
    recipients = ListField()

    def __str__(self):
        return self.subject

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        email_fields = re.split('\s\$\$\s', self.content)
        template_fields = self.template.fields
        # super().save(force_insert, force_update, using, update_fields)