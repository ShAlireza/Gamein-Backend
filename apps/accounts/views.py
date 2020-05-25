from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSignUpSerializer


# Create your views here.


class LogoutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class SignUpAPIView(GenericAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request):
        from .services.send_verification_email import send_verification_email

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        send_date = timezone.now() + timezone.timedelta(seconds=5)

        send_verification_email.apply_async(
            [serializer.validated_data['email']],
            eta=send_date
        )

        serializer.save()

        return Response(
            data={'details': _('Activation email sent, check your email')},
            status=status.HTTP_200_OK
        )


class ResendActivationEmailAPIView(GenericAPIView):
    pass
