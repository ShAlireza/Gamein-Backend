# Generated by Django 3.0.6 on 2020-06-03 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_auto_20191227_1933'),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='document',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='resources.Document'),
            preserve_default=False,
        ),
    ]
