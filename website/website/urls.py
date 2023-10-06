from django.urls import include, path
from rest_framework import routers
from product import views
from product.views import LessonViewRecord

router = routers.DefaultRouter()

router.register(r'lesson', views.LessonViewSet)

# Подключите наш API, используя автоматическую маршрутизацию URL.
# Кроме того, мы включаем URL-адреса для входа в систему для доступного для просмотра API.

urlpatterns = [
    path('', include(router.urls)),
    path('lesson_view_record/', LessonViewRecord.as_view(), name='lesson_view_record'),
]
