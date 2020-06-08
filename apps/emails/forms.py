import re

from django.forms import ModelForm, forms

from apps.emails.models import Email


class EmailRecipientsForm(ModelForm):
    recipients_file = forms.FileField(allow_empty_file=True)

    class Meta:
        model = Email
        fields = '__all__'

    def save(self, commit=True):
        instance = super(EmailRecipientsForm, self).save(commit)
        context = dict()
        email_values = re.split(Email.TEMPLATE_FIELDS_SPLITTER, instance.values_of_fields)
        template_fields = instance.template.emailtemplatefield_set.all().values_list('field_name', flat=True)
        for (field, value) in zip(template_fields, email_values):
            context[field] = value
            instance.template.emailtemplatefield_set.filter(field_name=field).update(field_value=value)
        if not instance.subject:
            instance.subject = context.get('subject')
        instance.html_context = instance.template.html
        instance.text_context = instance.template.text
        return super().save(commit)
