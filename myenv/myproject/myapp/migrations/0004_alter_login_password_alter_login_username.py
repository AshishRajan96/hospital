# Generated by Django 5.0.2 on 2024-03-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]