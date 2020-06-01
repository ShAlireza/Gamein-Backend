from django.contrib import admin, messages
from django.db import models
from django.utils.translation import ngettext
from martor.widgets import AdminMartorWidget

from apps.emails.models import Mail, EmailTemplate
from apps.emails.tasks import SendEmailTask


@admin.register(Mail)
class EmailAdmin(admin.ModelAdmin):
    exclude = ('html_context', 'text_context')
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    actions = ['send_emails']

    def send_emails(self, request, queryset):
        [SendEmailTask().delay(html_message=email.html_context,
                               text_message=email.text_context,
                               subject=email.subject,
                               to=self.get_recipients_emails(email.recipients)) for email in queryset]
        self.message_user(request, ngettext(
            '%d email was successfully sent.',
            '%d emails were successfully sent.',
            len(queryset),
        ) % len(queryset), messages.SUCCESS)

    send_emails.short_description = "Send selected emails"

    def get_recipients_emails(self, recipients):
        return list(recipients.all().values_list('email', flat=True))


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    pass
