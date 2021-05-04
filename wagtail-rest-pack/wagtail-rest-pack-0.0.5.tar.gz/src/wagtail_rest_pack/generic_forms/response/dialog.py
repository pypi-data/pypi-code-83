from .response import FormResponse
from wagtail.core import blocks

class ShowDialogResponse(FormResponse):
    type= 'form_open_dialog'

    @staticmethod
    def block_definition() ->tuple:
        return ShowDialogResponse.type, blocks.StructBlock(local_blocks=[
            ('title', blocks.TextBlock(required=True, help_text="Titulek", max_length=40)),
            ('text', blocks.StreamBlock([
                ('richtext', blocks.RichTextBlock(icon="doc-full"))
            ]))
        ])
