# Generated by Django 5.0.4 on 2024-05-03 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Entry title')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=40, null=True, verbose_name='Phone/Cell Number')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email Address')),
                ('address', models.TextField(null=True, verbose_name='Address')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Modified on')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
