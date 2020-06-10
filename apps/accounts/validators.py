from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from rest_framework.serializers import ValidationError as rest_ValidationError


def username_validator(value):
    try:
        validator = UnicodeUsernameValidator(value)
        validator(value)
    except ValidationError as e:
        raise rest_ValidationError(e.message)
