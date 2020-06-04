from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Lesson


class LessonsTitlesAPIView(GenericAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()

    def get(self, request):
        data = self.get_serializer(
            self.get_queryset().filter(role=request.user.role), many=True).data

        return Response(data={'lessons': data},
                        status=status.HTTP_200_OK)


class LessonAPIView(GenericAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()

    def get(self, request, lesson_id):
        lesson = get_object_or_404(self.get_queryset(), id=lesson_id)
        data = self.get_serializer(lesson).data
        return Response(data={'lesson': data}, status=status.HTTP_200_OK)
