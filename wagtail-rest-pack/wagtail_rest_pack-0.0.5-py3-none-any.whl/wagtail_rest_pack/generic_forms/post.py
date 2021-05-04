from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from wagtail_rest_pack.generic_forms.models import FormBuilder
from .models import FormBuilder


class PostFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    action = serializers.CharField(max_length=30)

    class Meta:
        fields = ['name', 'action', ]

    def create(self, validated_data):
        return super(PostFormSerializer, self).create(validated_data)


class PostFormView(APIView):
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'name'
    queryset = FormBuilder.objects.all()

    def get_serializer(self, *args, **kwargs):
        return PostFormSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, *args, **kwargs)
        if serializer.is_valid():
            data = serializer.validated_data
            form: FormBuilder = self.queryset.get(name=data['name'])
            serializer.save()
            return HttpResponse('cajk')
        return HttpResponseBadRequest(serializer.errors['name'])
