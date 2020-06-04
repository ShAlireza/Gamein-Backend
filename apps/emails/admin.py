import string

from django.contrib import admin, messages
from django.db import models
from django.template import Context, Template
from django.utils.translation import ngettext
from martor.widgets import AdminMartorWidget

from apps.accounts.models import Profile
from apps.emails.models import Email, EmailTemplate, EmailTemplateKeywords
from apps.emails.tasks import SendEmailTask


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    exclude = ('html_context', 'text_context')
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    actions = ['send_emails']

    def send_emails(self, request, queryset):
        for email in queryset:
            email_keywords = email.template.emailtemplatekeywords_set
            if email_keywords:
                self.send_email_with_keyword(email)
            else:
                self.send_email_without_keyword(email)

        self.message_user(request, ngettext(
            '%d email was successfully sent.',
            '%d emails were successfully sent.',
            len(queryset),
        ) % len(queryset), messages.SUCCESS)

    def send_email_without_keyword(self, email):
        self.set_values_to_template_fields(email)
        self.call_send_email_task(email, email.recipients)

    def send_email_with_keyword(self, email):
        email_keywords = email.template.emailtemplatekeywords_set.values_list('keyword_type', flat=True)
        for recipient in email.recipients.all():
            for email_keyword in email_keywords:
                keyword_regex = self.get_keyword_regex(email_keyword)
                if email_keyword == EmailTemplateKeywords.USER_NAME:
                    self.handle_user_name_keyword(email, recipient, keyword_regex)
                elif email_keyword == EmailTemplateKeywords.USER_UNIVERSITY:
                    self.handle_user_university_keyword(email, recipient, keyword_regex)
                elif email_keyword == EmailTemplateKeywords.USER_FELLOW_STUDENT:
                    self.handle_user_fellow_students_keyword(email, recipient, keyword_regex)
            self.set_values_to_template_fields(email)
            self.call_send_email_task(email, [recipient.user.email])

    def set_values_to_template_fields(self, email):
        template = email.template
        context = dict()
        for field in template.emailtemplatefield_set.all():
            context.update({field.field_name: field.field_value})
        email.html_context = self.render_email_templates(email.html_context, context)
        email.text_context = self.render_email_templates(email.text_context, context)

    def render_email_templates(self, template: string, context: dict):
        return Template(template).render(Context(context))

    def handle_user_fellow_students_keyword(self, email, recipient, keyword_regex):
        fellow_students = self.get_fellow_students(recipient)
        email.html_context.replace(keyword_regex, fellow_students, 1)

    def handle_user_university_keyword(self, email, recipient, keyword_regex):
        email.html_context = email.html_context.replace(keyword_regex, recipient.university, 1)

    def handle_user_name_keyword(self, email, recipient, keyword_regex):
        email.html_context = email.html_context.replace(keyword_regex, recipient.user.first_name, 1)

    def get_fellow_students(self, recipient):
        fellow_students_string = ''
        fellow_students = Profile.objects.filter(university=recipient.university)
        for fellow_student in fellow_students:
            fellow_students_string = fellow_students_string.__add__(fellow_student.__str__())
        return fellow_students_string

    def call_send_email_task(self, email: Email, to: list):
        SendEmailTask().apply_async(args=[email.html_context,
                                          email.text_context,
                                          email.subject,
                                          to])

    def get_recipients_emails(self, recipients):
        recipient_emails = list()
        [recipient_emails.append(recipient.user.email) for recipient in recipients.all()]
        return recipient_emails

    def get_keyword_regex(self, email_keyword):
        for KEYWORD, VALUE in EmailTemplateKeywords.KEYWORDS:
            if email_keyword == KEYWORD:
                return '{{ ' + VALUE + ' }}'

    send_emails.short_description = "Send selected emails"


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    pass
