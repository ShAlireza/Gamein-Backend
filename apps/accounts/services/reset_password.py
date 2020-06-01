import secrets
from typing import Union

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from ..models import ResetPasswordToken

__all__ = ('ResetPassword',)


class ResetPassword:

    def __init__(self, user: User):
        self.user: User = user
        self.uid: str = urlsafe_base64_encode(force_bytes(user.id))
        self._reset_password_token: Union[None, ResetPasswordToken] = None

    def reset_password(self) -> None:
        self._cancel_previous_tokens()
        self._create_reset_password_token()
        self._send_email()

    def _cancel_previous_tokens(self) -> None:
        (ResetPasswordToken.objects.
         filter(self.uid).
         filter(expired=False).
         update(expired=True)
         )

    def _create_reset_password_token(self) -> None:
        self._reset_password_token = ResetPasswordToken.objects.create(
            uid=self.uid,
            token=secrets.token_urlsafe(32),
            expiration_date=timezone.now() + timezone.timedelta(
                seconds=ResetPasswordToken.EXPIRATION_TIME)
        )

    def _send_email(self) -> None:
        from django.conf import settings
        from apps.core.utils import send_email

        context = {
            'domain': settings.DOMAIN,
            'username': self.user.username,
            'uid': self.uid,
            'token': self._reset_password_token.token,
        }

        send_email(
            subject=f'Reset password in {"Gamein Challenge"}',
            template_name='accounts/user_reset_password.html',
            context=context,
            receipts=[self.user.email]
        )
