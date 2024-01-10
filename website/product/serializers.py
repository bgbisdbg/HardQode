from rest_framework import serializers

class ProductStatisticSerializer(serializers.Serializer):
    title = serializers.CharField()
    lesson_view_count = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    total_user_on_products = serializers.IntegerField()
    purchasing_percent = serializers.FloatField()