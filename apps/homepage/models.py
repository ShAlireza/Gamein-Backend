from django.db import models



class Staff(models.Model):

    name = models.CharField(max_length=64)
    family_name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to="staff_pictures")
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=32)
    # major = models.CharField(max_length=128)

