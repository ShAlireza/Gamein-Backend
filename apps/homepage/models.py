from django.db import models
from .storage import OverwriteStorage


class Staff(models.Model):

    def upload_path(self, filename):
        ext = filename.split('.')[-1]
        return f'staff_pictures/{self.team}/{self.name}_{self.last_name}.{ext}'

    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    team = models.ForeignKey('StaffTeam', on_delete=models.SET_NULL, null=True, blank=True)
    picture = models.ImageField(upload_to=upload_path, storage=OverwriteStorage(),
                                default='staff_pictures/profile.jpg', blank=True)
    role = models.CharField(max_length=20, blank=True)
    linked_in_url = models.URLField('Linked-in', blank=True)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Sponsor(models.Model):
    def upload_path(self, filename):
        ext = filename.split('.')[-1]
        return f'sponsor_pictures/{self.name}.{ext}'
    SponsorClass = models.TextChoices('Sponsor Class', '1 2 3')
    name = models.CharField(max_length=100)
    sponsor_class = models.CharField(max_length=100, choices=SponsorClass.choices)
    picture = models.ImageField(upload_to=upload_path)
    site_url = models.URLField('WebSite')

    def __str__(self):
        return self.name


class Winner(models.Model):
    title = models.CharField(max_length=100)
    award = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


class Quote(models.Model):
    quoter = models.CharField(max_length=100, default='ناشناس')
    context = models.TextField()

    def __str__(self):
        return  'نقل از ' + self.quoter

class Event(models.Model):
    title = models.CharField(max_length=100)
    persian_date = models.CharField(max_length=50)
    date = models.DateTimeField()
    countdownable = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Statistics(models.Model):
    title = models.CharField(max_length=100)
    stat = models.IntegerField()
    icon = models.ImageField(upload_to='stat_icons')


class Social(models.Model):
    def upload_path(self, filename):
        ext = filename.split('.')[-1]
        return f'social_icons/{self.name}.{ext}'

    name = models.CharField(max_length=100, blank=True)
    url = models.URLField()
    icon = models.ImageField(upload_to=upload_path, storage=OverwriteStorage())

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100, blank=True)
    context = models.TextField()


class StaffTeam(models.Model):
    team_name = models.CharField(max_length=100)
    head = models.OneToOneField(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.team_name


class Video(models.Model):
    def upload_path(self, filename):
        ext = filename.split('.')[-1]
        return f'home_page_videos/{self.title}.{ext}'
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to=upload_path, storage=OverwriteStorage())

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question[:10] + '...'