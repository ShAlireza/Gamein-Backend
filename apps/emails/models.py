from django.db import models
from martor.models import MartorField
from rest_framework.fields import ListField


class Email(models.Model):
    subject = models.CharField(null=False, max_length=100)
    content = models.TextField(null=False)
    recipients = ListField()

    def __str__(self):
        return self.subject


class EmailTemplate(models.Model):
    title = models.CharField(null=False, max_length=50)
    html = MartorField()
    text = models.TextField(null=False)

    def __str__(self):
        return self.title
