# Generated by Django 3.0.6 on 2020-06-04 10:22

from django.db import migrations, models
import django.db.models.deletion
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('html', martor.models.MartorField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplateKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_type', models.CharField(choices=[('UN', 'user.name'), ('UU', 'user.university'), ('UFS', 'user.fellow_students')], default=None, max_length=4)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.EmailTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplateField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.TextField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.EmailTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('values_of_fields', models.TextField()),
                ('html_context', models.TextField()),
                ('text_context', models.TextField()),
                ('recipients', models.ManyToManyField(to='accounts.Profile')),
                ('template', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emails.EmailTemplate')),
            ],
        ),
    ]
