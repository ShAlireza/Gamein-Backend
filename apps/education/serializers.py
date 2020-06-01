from rest_framework import serializers

from apps.education.models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = Lesson
        fields = ['name', 'order', 'document', 'is_open', 'is_read', 'role']
