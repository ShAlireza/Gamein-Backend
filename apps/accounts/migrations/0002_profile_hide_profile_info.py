# Generated by Django 3.0.6 on 2020-05-29 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hide_profile_info',
            field=models.BooleanField(default=False),
        ),
    ]
