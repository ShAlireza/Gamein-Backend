from django import forms

from apps.accounts.models import Profile
from apps.emails.models import Email

import re


class EmailRecipientsForm(forms.ModelForm):
    EMAILS_FILE_SPLIT_PATTERN = '[\r]?[\n]?'

    NONE_OF_THESE = 'none_of_these'
    ALL = 'all_users'
    OPTIONS_CHOICES = [
        (NONE_OF_THESE, 'None Of These'),
        (ALL, 'All Of The Users'),
    ]
    recipients_file = forms.FileField(allow_empty_file=True, required=False)
    recipients_options = forms.ChoiceField(choices=OPTIONS_CHOICES, widget=forms.RadioSelect,
                                           required=False,
                                           label='Send Email to')

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
        option = self.cleaned_data['recipients_options']
        if option and option != self.NONE_OF_THESE:
            if option == self.ALL:
                self.set_all_users_as_recipient(self.instance)
        file = self.cleaned_data['recipients_file']
        if file:
            for chunk in file.chunks():
                emails = self.get_emails_from_file_chunk(chunk.decode('utf-8'))
                self.get_recipients_users_by_email_addresses(self.instance, emails)
        super(EmailRecipientsForm, self)._save_m2m()

    def get_emails_from_file_chunk(self, chunk):
        return re.split(self.EMAILS_FILE_SPLIT_PATTERN, chunk)

    def get_recipients_users_by_email_addresses(self, email: Email, recipients: list):
        for recipient in recipients:
            recipient_profile = Profile.objects.filter(user__email=recipient).first()
            email.recipients.add(recipient_profile)

    def set_all_users_as_recipient(self, email):
        all_users = Profile.objects.all()
        [email.recipients.add(user) for user in all_users]
