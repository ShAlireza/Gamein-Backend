# Generated by Django 3.0.6 on 2020-05-28 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_event_statistics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='family_name',
            new_name='last_name',
        ),
    ]