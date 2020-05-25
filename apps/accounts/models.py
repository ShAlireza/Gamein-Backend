from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)

    university = models.CharField(max_length=64)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=32)


class ResetPasswordToken(models.Model):
    uid = models.CharField(max_length=128)
    token = models.CharField(max_length=128)
    expiration_date = models.DateField()


class ActivateUserToken(models.Model):
    token = models.CharField(max_length=128)
    eid = models.CharField(max_length=128, null=True)
