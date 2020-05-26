import secrets
from typing import Union

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from gamein_backend.celery import app

from ..models import ActivateUserToken

__all__ = ('send_activation_email',)


class SendActivationEmail:
    def __init__(self, email: str):
        self.email: str = email
        self._activation_token: Union[None, ActivateUserToken] = None

    def send_activation_email(self):
        self._create_activation_token()
        self._send_email()
        pass

    def _create_activation_token(self) -> None:
        self._activation_token = ActivateUserToken.objects.create(
            token=secrets.token_urlsafe(32),
            eid=urlsafe_base64_encode(
                force_bytes(self.email)),
        )

    def _send_email(self) -> None:
        from django.conf import settings
        from apps.core.utils import send_email

        context = {
            'domain': settings.DOMAIN,
            'eid': self._activation_token.eid,
            'token': self._activation_token.token,
        }

        send_email(
            subject=f'Account activation in {"Gamein Challenge"}',
            template_name='accounts/activation_email.html',
            context=context
        )


@app.task(name='send_verification_email')
def send_activation_email(user_email: str) -> None:
    send_activiation_email_service = SendActivationEmail(user_email)
    send_activiation_email_service.send_activation_email()
