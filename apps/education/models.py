from django.db import models


class Role(models.Model):
    title = models.CharField(max_length=64)


class Lesson(models.Model):
    name = models.CharField(max_length=64)
    order = models.PositiveSmallIntegerField()
    # document = models.OneToOneField('',
    #                                 on_delete=models.CASCADE)
    is_open = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    role = models.ForeignKey('education.Role', on_delete=models.CASCADE)
