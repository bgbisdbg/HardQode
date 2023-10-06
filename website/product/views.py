from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import LessonProduct
from product.serializers import AllLesson

from django.shortcuts import render
from django.views import View
from .models import LessonProduct

class LessonViewRecord(View):
    def post(self, request):
        lesson_id = request.POST.get('lesson_id')
        view_time = request.POST.get('view_time')

        # Получаем продолжительность урока
        lesson = LessonProduct.objects.get(pk=lesson_id)
        duration = lesson.duration

        percent_watched = (float(view_time) / duration) * 100

        status = "Просмотрено" if percent_watched >= 80 else "Не просмотрено"

        # Записываем данные просмотра урока в базу данных
        view = LessonProduct(lesson_id=lesson_id, view_time=view_time, status=status)
        view.save()

        return render(request, 'lesson_view_record.html', {'status': status})



class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = LessonProduct.objects.all()
    serializer_class = AllLesson
    permission_classes = [permissions.IsAuthenticated]
