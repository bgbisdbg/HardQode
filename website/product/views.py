from django.contrib.auth.models import User
from django.db.models import Count, OuterRef, Sum, F
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from product.models import Product, ProductAccess
from product.serializers import ProductStatisticSerializer
from study.models import LessonViewInfo, LessonStatus


class ProductStatisticViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ProductStatisticSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, )

    def get_queryset(self):
        total_users_count = User.objects.filter(is_active=True).count()

        qs = Product.objects.all().annotate(
            lesson_view_count=Count(
                LessonViewInfo.objects.filter(
                    lesson__products=OuterRef('id'),
                    status=LessonStatus.VIEWED
                ).values('id')
            ),
            total_view_time=Sum(
                LessonViewInfo.objects.filter(
                    lesson__products=OuterRef('id'),
                ).values('view_time')
            ),
            total_user_on_products=Count(
                ProductAccess.objects.filter(product_id=OuterRef('id')).values('id')
            ),
            purchasing_percent=F('total_user_on_products') / float(total_users_count) * 100
        )

        return qs