
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import get_recaptcha_instance

from rest_framework.exceptions import ValidationError

class AuthenticatedOrRecaptcha(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        try:
            get_recaptcha_instance().verify(request)
            return True
        except ValidationError:
            return False

