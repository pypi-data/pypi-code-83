from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.core.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail_rest_pack.generic_forms.blocks.group_block import GroupBlockSerializer
from wagtail_rest_pack.generic_forms.blocks.submit_block import SubmitBlockSerializer
from wagtail_rest_pack.generic_forms.blocks.text_block import InputBlockSerializer

security_choices = [
    ('recaptcha_or_user', 'Recaptcha nebo přihlášený uživatel.'),
    ('authenticated_user_only', 'Přihlášený uživatel pouze.')
]


@register_snippet
class FormBuilder(ClusterableModel):
    name = models.CharField(max_length=60, validators=[], primary_key=True)
    display_name = models.TextField(max_length=100, default="")
    description = models.TextField(max_length=1000, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    security = models.CharField(max_length=30, default="recaptcha_or_user", choices=security_choices)

    stream = StreamField(block_types=[
        InputBlockSerializer.block_definition(),
        GroupBlockSerializer.block_definition(),
        SubmitBlockSerializer.block_definition(),
    ])

    def __str__(self):
        return 'Formulář "{}"'.format(self.display_name)
