from rest_framework import serializers

from .models import Role, Lesson


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = ('id',)


class LessonSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = Lesson
        fields = ('name', 'order', 'document', 'is_open', 'is_read', 'role')
