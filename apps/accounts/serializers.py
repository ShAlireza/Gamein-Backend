from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('university', 'birth_date', 'phone_number')


class UserSignUpSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])

    password_1 = serializers.CharField(style={'input_type': 'password'})
    password_2 = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password_1', 'password_2', 'profile')

    def validate(self, data):
        if data['password_1'] != data['password_2']:
            raise serializers.ValidationError('passwords don\'t match!')
        return data

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        profile_data = validated_data.pop('profile')
        validated_data.pop('password_1')
        validated_data['password'] = make_password(
            validated_data.pop('password_2'))
        validated_data['is_active'] = False

        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)

        return user
