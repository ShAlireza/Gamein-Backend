# Generated by Django 3.0.7 on 2020-06-08 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
    ]