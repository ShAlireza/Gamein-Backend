from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import (UserSignUpSerializer, EmailSerializer,
                          ResetPasswordConfirmSerializer,
                          ActivateUserTokenSerializer,
                          ChangePasswordSerializer, ProfileSerializer)


# Create your views here.


class LogoutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class SignUpAPIView(GenericAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request):
        from .tasks import send_activation_email

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        send_date = timezone.now() + timezone.timedelta(seconds=5)

        send_activation_email.apply_async(
            [serializer.validated_data['email']],
            eta=send_date
        )

        serializer.save()

        return Response(
            data={'details': _('Activation email sent, check your email')},
            status=status.HTTP_200_OK
        )


class ResendActivationEmailAPIView(GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        from .tasks import send_activation_email

        data = self.get_serializer(data=request.data).data
        user = get_object_or_404(User, email=data['email'])

        send_date = timezone.now() + timezone.timedelta(seconds=5)
        send_activation_email.apply_async(
            [user.email],
            eta=send_date
        )

        return Response(
            data={'details': _('Activation email sent, check your email')},
            status=status.HTTP_200_OK
        )


class ActivateAccountAPIView(GenericAPIView):
    serializer_class = ActivateUserTokenSerializer

    def post(self, request):
        from .services.activate_account import ActivateAccount

        data = self.get_serializer(data=request.data).data
        activate_account_service = ActivateAccount(eid=data['eid'],
                                                   token=data['token'])
        activate_account_service.activate()

        return Response(
            data={'details': _('Account successfully activated!')},
            status=status.HTTP_200_OK
        )


class ResetPasswordAPIView(GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        from .tasks import reset_password

        data = self.get_serializer(data=request.data).data
        user = get_object_or_404(User, email=data['email'])

        send_date = timezone.now() + timezone.timedelta(seconds=5)
        reset_password.apply_async(
            [user.id],
            eta=send_date
        )

        return Response(
            data={'details': _('Reset password email sent, check your email')},
            status=status.HTTP_200_OK
        )


class ResetPasswordConfirmAPIView(GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer

    def post(self, request):
        from .services.reset_password_confirm import ResetPasswordConfirm

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        reset_password_confirm_service = ResetPasswordConfirm(
            uid=data['uid'],
            token=data['token'],
            password=data['password']
        )
        reset_password_confirm_service.reset_password_confirm()

        return Response(
            data={'details': _('Password changed successfully')},
            status=status.HTTP_200_OK
        )


class ChangePasswordAPIView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={'details': _('Password changed successfully')},
            status=status.HTTP_200_OK
        )


class ToggleProfileInfoVisibilityAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        profile = request.user.profile
        profile.hide_profile_info = not profile.hide_profile_info
        profile.save()

        return Response(
            data={'details': _('Profile updated successfully')},
            status=status.HTTP_200_OK
        )


class ProfileInfoAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get(self, request):
        profile = request.user.profile
        data = self.get_serializer(profile).data
        return Response(data={'profile': data}, status=status.HTTP_200_OK)
