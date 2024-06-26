# Generated by Django 5.0.4 on 2024-05-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactentry',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='contactentry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='contactentry',
            name='phone_number',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Phone/Cell Number'),
        ),
    ]
