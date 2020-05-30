from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from apps.emails.models import EmailContent


@admin.register(EmailContent)
class EmailContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
