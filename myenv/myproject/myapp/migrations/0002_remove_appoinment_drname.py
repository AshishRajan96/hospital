# Generated by Django 5.0.2 on 2024-03-06 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoinment',
            name='drname',
        ),
    ]