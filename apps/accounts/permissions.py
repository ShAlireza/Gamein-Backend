from rest_framework.permissions import BasePermission


class HasCompletedProfile(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and hasattr(request.user, 'profile'))
