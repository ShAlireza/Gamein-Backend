from django.db import models


class UserRoleContent(models.Model):
    title = models.CharField(max_length=64)


class Lesson(models.Model):
    name = models.CharField(max_length=64)
    order = models.PositiveSmallIntegerField()
    document = models.OneToOneField('education.UserRoleContent',
                                    on_delete=models.CASCADE)
    is_open = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    role = models.ForeignKey('', on_delete=models.CASCADE)
