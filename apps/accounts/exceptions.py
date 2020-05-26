from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework import status


class PasswordsNotMatch(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Entered passwords don't match")
    default_code = _("passwords_not_match")


class TokenExpired(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("Token expired")
    default_code = _("token_expired")
