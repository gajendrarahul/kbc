# Generated by Django 3.0.5 on 2021-04-29 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20210427_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_teacehr',
            new_name='is_teacher',
        ),
    ]