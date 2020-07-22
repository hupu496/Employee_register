# Generated by Django 3.0.5 on 2020-04-07 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.DateField(default=34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
