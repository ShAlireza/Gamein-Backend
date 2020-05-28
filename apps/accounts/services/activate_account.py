from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode

from rest_framework.generics import get_object_or_404

from apps.accounts.models import ActivateUserToken
from ..exceptions import AccountActivationError

__all__ = ('ActivateAccount',)


class ActivateAccount:

    def __init__(self, eid: str, token: str):
        self.eid: str = eid
        self.token: str = token
        self._activate_user_token = get_object_or_404(ActivateUserToken,
                                                      eid=eid, token=token)
        self._email = urlsafe_base64_decode(eid).decode('utf-8')

    def activate(self):
        self._activate_user()

    def _activate_user(self):
        try:
            user = User.objects.get(email=self._email)
        except User.DoesNotExist:
            raise AccountActivationError()

        user.is_active = True
        user.save()
        self._activate_user_token.delete()
