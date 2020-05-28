from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator

from .models import Profile, ResetPasswordToken, ActivateUserToken
from .exceptions import PasswordsNotMatch, WrongPassword


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('university', 'birth_date', 'phone_number', 'major')


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
            raise PasswordsNotMatch()
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


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordConfirmSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    password_repeat = serializers.CharField(max_length=100)

    class Meta:
        model = ResetPasswordToken
        fields = ('password', 'password_repeat', 'uid', 'token')

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise PasswordsNotMatch()

        return data


class ActivateUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivateUserToken
        fields = ('token', 'eid')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type': 'password'})
    new_password = serializers.CharField(style={'input_type': 'password'})
    new_password_repeat = serializers.CharField(
        style={'input_type': 'password'})

    def validate(self, data):
        if data['new_password'] != data['new_password_repeat']:
            raise PasswordsNotMatch()
        if not self.context['request'].check_password(data['old_password']):
            raise WrongPassword()

    def save(self, **kwargs):
        self.context['request'].user.set_password(
            self.validated_data['new_password']
        )
        self.context['request'].user.save()

        return self.context['request'].user
