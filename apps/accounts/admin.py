from django.contrib import admin

from .models import Profile, ResetPasswordToken, ActivateUserToken


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ResetPasswordToken)
class ResetPasswordTokenAdmin(admin.ModelAdmin):
    pass


@admin.register(ActivateUserToken)
class ActivateUserTokenAdmin(admin.ModelAdmin):
    pass
