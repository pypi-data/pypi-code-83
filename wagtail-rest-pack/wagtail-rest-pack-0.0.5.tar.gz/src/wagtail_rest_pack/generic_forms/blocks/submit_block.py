from rest_framework import serializers
from wagtail.core import blocks
from wagtail_rest_pack.generic_forms.actions.send_email import SendEmailAction
from wagtail_rest_pack.generic_forms.response.snack import ShowSnackResponse
from wagtail_rest_pack.generic_forms.response.dialog import ShowDialogResponse


class SubmitBlockSerializer(serializers.Serializer):
    block_name = 'form_submit'
    name = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=30)

    @staticmethod
    def block_definition():
        return SubmitBlockSerializer.block_name, SubmitBlock('submit')

    class Meta:
        fields = ('name', 'text',)




class SubmitBlock(blocks.StructBlock):

    def get_responses(self):
        return [
            ShowDialogResponse.block_definition(),
            ShowSnackResponse.block_definition(),
        ]

    def get_actions(self):
        return [
            SendEmailAction.block_definition(),
        ]

    def __init__(self, *args, **kwargs):
        self.action_definitions = blocks.StreamBlock(self.get_actions(), min_num=1, max_num=1, label="Akce")
        self.response_definition = blocks.StreamBlock(self.get_responses(), min_num=1, max_num=1, label="Odpověď")
        super().__init__(local_blocks=[
            ('name', blocks.TextBlock(max_length=30, help_text="Název pole v ascii (např. user_email)", label="Jméno", validators=[])),
            ('text', blocks.CharBlock(max_length=30, label="Text na tlačítku")),
            ('action', self.action_definitions),
            ('response', self.response_definition)
        ], **kwargs)
