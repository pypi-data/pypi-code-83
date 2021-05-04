from wagtail_rest_pack.generic_forms.blocks.generic_input import GenericInputBlock
from django.core.exceptions import ValidationError
from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet
from django.db import models
from rest_framework import serializers
from wagtail.core import blocks

from wagtail.core.fields import StreamField


class InputBlockSerializer(serializers.Serializer):

    block_name = 'form_text'

    @staticmethod
    def block_definition():
        return InputBlockSerializer.block_name, GenericInputBlock(specific=[
            ('multiline', blocks.BooleanBlock(required=False, help_text="Víceřádkový vstup."))
        ])

    def to_representation(self, instance):
        return instance