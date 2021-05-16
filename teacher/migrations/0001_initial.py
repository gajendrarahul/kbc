# Generated by Django 3.0.5 on 2021-04-25 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('started_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('salary', models.PositiveIntegerField()),
                ('contact', phone_field.models.PhoneField(blank=True, help_text='Contact number', max_length=31)),
                ('address', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
