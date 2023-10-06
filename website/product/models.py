from django.db import models
from django.contrib.auth.models import User


class TheEssenceOfTheProduct(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(TheEssenceOfTheProduct, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.access_level}'


class TheEssenceOfTheLesson(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    lessons = models.ManyToManyField(TheEssenceOfTheLesson, through='LessonProduct')

    def __str__(self):
        return f'{self.id}'


class LessonProduct(models.Model):
    lesson = models.ForeignKey(TheEssenceOfTheLesson, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    view_time = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='Не просмотрено')

    def __str__(self):
        return f'{self.lesson} - {self.status} - {self.view_time}'
