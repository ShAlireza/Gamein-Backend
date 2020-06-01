from rest_framework.generics import GenericAPIView

from apps.education.models import *


class RoleSerializers(GenericAPIView):
    class Meta:
        model = Role
        fields = '__all__'


class LessonSerializers(GenericAPIView):
    role = RoleSerializers()

    class Meta:
        model = Lesson
        fields = ['name', 'order', 'document', 'is_open', 'is_read', 'role']
