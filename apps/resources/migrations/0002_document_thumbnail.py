# Generated by Django 2.2.8 on 2019-12-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='document/thumbnails/'),
        ),
    ]
