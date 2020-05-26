from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.http import urlsafe_base64_decode
from rest_framework.generics import get_object_or_404

from ..models import ResetPasswordToken
from ..exceptions import TokenExpired

__all__ = ('reset_password_confirm',)


class ResetPasswordConfirm:

    def __init__(self, uid: str, token: str, password: str):
        self.uid: str = uid
        self.token: str = token
        self.password: str = password
        self._reset_password_token: ResetPasswordToken = \
            get_object_or_404(ResetPasswordToken, uid=uid, token=token)

    def reset_password_confirm(self) -> None:
        self._check_expiration()
        self._change_password()

    def _check_expiration(self) -> None:
        if timezone.now() > self._reset_password_token.expiration_date:
            self._reset_password_token.make_expired()

            raise TokenExpired()

    def _change_password(self) -> None:
        self._reset_password_token.make_expired()
        user = get_object_or_404(
            User,
            id=urlsafe_base64_decode(self.uid).decode(
                'utf-8')
        )

        user.set_password(self.password)
        user.save()


def reset_password_confirm(uid: str, token: str, password: str) -> None:
    reset_password_confirm_service = ResetPasswordConfirm(
        uid, token, password
    )
    reset_password_confirm_service.reset_password_confirm()
