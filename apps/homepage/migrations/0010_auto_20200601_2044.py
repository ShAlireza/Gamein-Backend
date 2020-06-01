# Generated by Django 3.0.6 on 2020-06-01 20:44

import apps.homepage.models
import apps.homepage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20200529_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='picture',
            field=models.ImageField(blank=True, default='staff_pictures/profile.jpg', storage=apps.homepage.storage.OverwriteStorage(), upload_to=apps.homepage.models.Staff.upload_path),
        ),
    ]