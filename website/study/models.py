from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Lesson(models.Model):
    title = models.CharField(max_length=32)
    link = models.URLField()
    viewing_duration = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)


class LessonStatus(models.TextChoices):
    VIEWED = 'VIEWED'
    NOT_VIEWED = 'NOT_VIEWED'


class LessonViewInfo(models.Model):
    lesson = models.ForeignKey(Lesson, models.CASCADE, 'views')
    user = models.ForeignKey(User, models.CASCADE)
    status = models.CharField(choices=LessonStatus.choices, default=LessonStatus.NOT_VIEWED, max_length=32)
    view_time = models.IntegerField(default=0)
    last_view_datetime = models.DateTimeField(default=datetime.now())

    class Meta:
        unique_together = ('lesson', 'user')