from rest_framework import serializers
from product.models import LessonProduct


class AllLesson(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LessonProduct
        fields = ['lesson, status, view_time']


