from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from apps.emails.models import Email, EmailTemplate


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    exclude = ('html_context', 'text_context')
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    pass
