from django.db import models
from martor.models import MartorField
from rest_framework.fields import ListField, DictField
from apps.accounts.models import Profile

import re


class EmailTemplate(models.Model):
    title = models.CharField(null=False, max_length=50)
    html = MartorField()
    text = models.TextField(null=False)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        fields = self.find_template_variables(self.html)
        for field in fields:
            EmailTemplateField.objects.create(force_name=field, template=self)
        super().save(force_insert, force_update, using, update_fields)

    def find_template_variables(self, template):
        fields = re.findall('{{\s(\w+)\s}}', template)
        return fields


class EmailTemplateField(models.Model):
    field_name = models.TextField()
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)


class Email(models.Model):
    template = models.OneToOneField(to=EmailTemplate, on_delete=models.CASCADE)
    subject = models.CharField(null=False, max_length=100)
    content = models.TextField(null=False)
    recipients = ListField()

    def __str__(self):
        return self.subject
