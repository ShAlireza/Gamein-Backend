from django.db import models
from apps.accounts.models import Profile

import re


class EmailTemplate(models.Model):
    FIELDS_REGEX = '{{\s(\w+)\s}}'
    KEYWORDS_REGEX = '{{\s(\w+\.\w+)\s}}'

    title = models.CharField(null=False, max_length=50)
    html = models.TextField(null=False)
    text = models.TextField(null=False)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        fields = self.find_template_variables(self.html)
        keywords = self.find_template_keywords(self.html)
        EmailTemplateField.objects.filter(template=self).delete()
        EmailTemplateKeywords.objects.filter(template=self).delete()
        [EmailTemplateField.objects.create(field_name=field, field_value=None, template=self) for field in fields]
        [EmailTemplateKeywords.objects.create(keyword_type=keyword, template=self) for keyword in
         keywords]

    def find_template_variables(self, template):
        fields = re.findall(self.FIELDS_REGEX, template)
        return fields

    def find_template_keywords(self, template):
        keywords = re.findall(self.KEYWORDS_REGEX, template)
        for i in range(len(keywords)):
            for KEYWORD, VALUE in EmailTemplateKeywords.KEYWORDS:
                if keywords[i] == VALUE:
                    keywords[i] = KEYWORD
                    break
        return keywords


class EmailTemplateKeywords(models.Model):
    USER_NAME = 'UN'
    USER_UNIVERSITY = 'UU'
    USER_FELLOW_STUDENT = 'UFS'
    KEYWORDS = [
        (USER_NAME, 'user.name'),
        (USER_UNIVERSITY, 'user.university'),
        (USER_FELLOW_STUDENT, 'user.fellow_students')
    ]
    keyword_type = models.CharField(
        max_length=4,
        choices=KEYWORDS,
        default=None,
    )
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)


class EmailTemplateField(models.Model):
    field_name = models.TextField()
    field_value = models.TextField(blank=True, null=True)
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)


class Email(models.Model):
    TEMPLATE_FIELDS_SPLITTER = '\s?\n?\$\$\s?\n?'

    template = models.ForeignKey(to=EmailTemplate, on_delete=models.CASCADE)
    subject = models.CharField(blank=True, null=True, max_length=100)
    values_of_fields = models.TextField(blank=False, null=False)
    html_context = models.TextField()
    text_context = models.TextField()
    recipients = models.ManyToManyField(to=Profile, blank=True)

    def __str__(self):
        return self.subject
