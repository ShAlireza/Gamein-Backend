from django.db import models



class Staff(models.Model):

    TeamNames = models.TextChoices('Team Name', 'Site Idea others')
    # TODO: complete all teams' names

    team = models.CharField(max_length=64, choices=TeamNames.choices)
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to="staff_pictures", default='staff_pictures/profile.jpg', blank=True)
    role = models.CharField(max_length=20, blank=True)
    linked_in_url = models.URLField('Linked-in', blank=True)


class Sponsor(models.Model):

    SponsorClass = models.TextChoices('Sponsor Class', 'gold silver bronze')

    name = models.CharField(max_length=100)
    sponsor_class = models.CharField(max_length=100, choices=SponsorClass.choices)
    picture = models.ImageField(upload_to="sponsor_pictures")
    site_url = models.URLField('WebSite')


class Winner(models.Model):
    title = models.CharField(max_length=100)
    award = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


class Quote(models.Model):
    quoter = models.CharField(max_length=100, default='ناشناس')
    context = models.TextField()


class Event(models.Model):
    title = models.CharField(max_length=100)
    persian_date = models.CharField(max_length=50)
    date = models.DateTimeField()


class Statistics(models.Model):
    title = models.CharField(max_length=100)
    stat = models.IntegerField()
    icon = models.ImageField(upload_to='stat_icons')





