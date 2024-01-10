from django.urls import path, include

from product.views import ProductStatisticViewSet

urlpatterns =[
    path('product-statistic/', ProductStatisticViewSet.as_view({'get': 'list'})),
]
