# Generated by Django 3.0.5 on 2021-04-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_teacehr',
            field=models.BooleanField(default=False),
        ),
    ]
