# Generated by Django 3.2.13 on 2024-01-10 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_lessonviewinfo_last_view_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonviewinfo',
            name='last_view_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 17, 18, 42, 462532)),
        ),
    ]