# Generated by Django 3.0.7 on 2020-06-09 05:04

import apps.homepage.models
import apps.homepage.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20200601_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(storage=apps.homepage.storage.OverwriteStorage(), upload_to=apps.homepage.models.Video.upload_path)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='countdownable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='icon',
            field=models.ImageField(storage=apps.homepage.storage.OverwriteStorage(), upload_to=apps.homepage.models.Social.upload_path),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='picture',
            field=models.ImageField(upload_to=apps.homepage.models.Sponsor.upload_path),
        ),
        migrations.CreateModel(
            name='StaffTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('head', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_count', models.IntegerField()),
                ('about', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.About')),
                ('events', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Event')),
                ('faq', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.FAQ')),
                ('quotes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Quote')),
                ('socials', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Social')),
                ('sponsors', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Sponsor')),
                ('staffs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Staff')),
                ('statistics', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Statistics')),
                ('videos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Video')),
                ('winners', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.Winner')),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.StaffTeam'),
        ),
    ]
