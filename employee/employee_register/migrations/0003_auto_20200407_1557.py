# Generated by Django 3.0.5 on 2020-04-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0002_auto_20200407_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
    ]
