from django.contrib import admin
from .models import *


class StaffAdmin(admin.ModelAdmin):
    list_display = ('family_name', 'name', 'team', 'role', 'picture', 'linked_in_url')


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sponsor_class', 'picture', 'site_url')


class WinnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'award')


admin.site.register(Staff, StaffAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Winner, WinnerAdmin)



