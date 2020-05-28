from django.db import models



class Staff(models.Model):

    team = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    family_name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to="staff_pictures")
    role = models.CharField(max_length=20)
    linked_in_url = models.URLField()





