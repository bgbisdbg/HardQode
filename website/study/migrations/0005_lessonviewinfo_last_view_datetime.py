# Generated by Django 3.2.13 on 2024-01-10 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_rename_product_lesson_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonviewinfo',
            name='last_view_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 10, 17, 1, 47, 998162)),
        ),
    ]