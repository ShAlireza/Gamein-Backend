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
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=150, required=True)

    password = serializers.CharField(style={'input_type': 'password'})
    password_repeat = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'password', 'password_repeat',
            'profile')

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError('passwords don\'t match!')
        return data

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        profile_data = validated_data.pop('profile')
        validated_data.pop('password_repeat')
        validated_data['password'] = make_password(
            validated_data.pop('password'))
        validated_data['is_active'] = False

        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)

        return user
