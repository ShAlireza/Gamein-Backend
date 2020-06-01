from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from apps.emails.models import Email, EmailTemplate


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    exclude = ('subject', )
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    pass
