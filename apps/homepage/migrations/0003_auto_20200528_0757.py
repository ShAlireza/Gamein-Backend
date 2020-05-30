# Generated by Django 3.0.6 on 2020-05-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20200528_0644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sponsor_class', models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver'), ('bronze', 'Bronze')], max_length=100)),
                ('picture', models.ImageField(upload_to='sponsor_pictures')),
                ('site_url', models.URLField(verbose_name='WebSite')),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='linked_in_url',
            field=models.URLField(verbose_name='Linked-in'),
        ),
    ]
