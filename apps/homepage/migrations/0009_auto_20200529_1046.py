# Generated by Django 3.0.6 on 2020-05-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20200528_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('context', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='sponsor_class',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100),
        ),
    ]
