from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)

    university = models.CharField(max_length=64)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=32)
    major = models.CharField(max_length=128)
    role = models.ForeignKey('education.Role', related_name='profiles',
                             on_delete=models.DO_NOTHING, blank=True,
                             null=True)

    def __str__(self):
        return self.user.get_full_name()


class ResetPasswordToken(models.Model):
    EXPIRATION_TIME = 24 * 60 * 60

    uid = models.CharField(max_length=128)
    token = models.CharField(max_length=128)
    expiration_date = models.DateField()

    expired = models.BooleanField(default=False)

    def make_expired(self):
        self.expired = True
        self.save()

    def __str__(self):
        return self.token


class ActivateUserToken(models.Model):
    token = models.CharField(max_length=128)
    eid = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.token
