import re

from django.forms import ModelForm, forms

from apps.accounts.models import Profile
from apps.emails.models import Email


class EmailRecipientsForm(ModelForm):
    EMAILS_FILE_SPLIT_PATTERN = '[\r]?[\n]?'
    recipients_file = forms.FileField(allow_empty_file=True, required=False)

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

    def _save_m2m(self):
        file = self.cleaned_data['recipients_file']
        for chunk in file.chunks():
            emails = self.get_emails_from_file_chunk(chunk.decode('utf-8'))
            self.set_emails_recipients(self.instance, emails)
        super(EmailRecipientsForm, self)._save_m2m()

    def get_emails_from_file_chunk(self, chunk):
        return re.split(self.EMAILS_FILE_SPLIT_PATTERN, chunk)

    def set_emails_recipients(self, email: Email, recipients: list):
        for recipient in recipients:
            recipient_profile = Profile.objects.filter(user__email=recipient).first()
            email.recipients.add(recipient_profile)
