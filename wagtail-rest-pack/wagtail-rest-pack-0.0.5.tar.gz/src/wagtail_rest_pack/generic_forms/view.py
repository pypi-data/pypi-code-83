
from rest_framework import serializers,generics
from rest_framework.permissions import AllowAny
from wagtail_rest_pack.streamfield.serializers import SettingsStreamFieldSerializer

from .models import FormBuilder
from wagtail.core.fields import StreamField
from wagtail.api.v2.serializers import Field




class GetFormBuilderSerializer(serializers.ModelSerializer):
    stream = SettingsStreamFieldSerializer()

    class Meta:
        model = FormBuilder
        fields = ['name', 'display_name', 'security', 'stream']


class FormView(generics.RetrieveAPIView):

    permission_classes = [AllowAny]
    queryset = FormBuilder.objects.all()
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    serializer_class = GetFormBuilderSerializer
