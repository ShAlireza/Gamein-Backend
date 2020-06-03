from django.contrib import admin

from .models import Profile, ResetPasswordToken, ActivateUserToken


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('university', 'major', 'hide_profile_info', 'role')
    search_fields = ('university', 'major')
    list_filter = ('university', 'major', 'role')


@admin.register(ResetPasswordToken)
class ResetPasswordTokenAdmin(admin.ModelAdmin):
    list_display = ('uid', 'token', 'expiration_date')
    list_filter = ('expiration_date', 'expired')


@admin.register(ActivateUserToken)
class ActivateUserTokenAdmin(admin.ModelAdmin):
    list_display = ('eid', 'token', 'used')
    list_filter = ('used',)
