
from rest_framework.exceptions import ValidationError
from wagtail_rest_pack.recaptcha.models import RecaptchaVerifier
from django.conf import settings
class NoopRecaptchaVerifier(RecaptchaVerifier):
    def verify(self, request):
        pass