# Generated by Django 3.0.5 on 2021-05-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacherdetails_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherdetails',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]