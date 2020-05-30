from django.db import models


class EmailContent(models.Model):
    subject = models.CharField(null=False, max_length=100)
    text = models.TextField(null=False)

    def __str__(self):
        return self.subject
