from django.contrib.auth.models import User

from apps.accounts.services.reset_password import ResetPassword
from apps.accounts.services.reset_password_confirm import ResetPasswordConfirm
from apps.accounts.services.send_verification_email import SendActivationEmail
from gamein_backend.celery import app


@app.task(name='send_verification_email')
def send_activation_email(user_email: str) -> None:
    send_activation_email_service = SendActivationEmail(user_email)
    send_activation_email_service.send_activation_email()


@app.task(name='reset_password')
def reset_password(user_id: int) -> None:
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        pass
    else:
        reset_password_service = ResetPassword(user=user)
        reset_password_service.reset_password()
