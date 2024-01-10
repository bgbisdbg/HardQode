from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('study/', include('study.urls')),
    path('product/', include('product.urls')),
]
