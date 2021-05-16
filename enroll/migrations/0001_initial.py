# Generated by Django 3.0.5 on 2021-04-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=100)),
                ('end_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('batch', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
