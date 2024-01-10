from django.urls import path, include
from rest_framework.routers import SimpleRouter

from study.views import MyLessonViewSet, MyLessonsByProductViewSet

router = SimpleRouter()
router.register('my-lessons', MyLessonViewSet, 'my-lessons')


urlpatterns =[
    path('by-product/<int:product_id>/lessons/', MyLessonsByProductViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
