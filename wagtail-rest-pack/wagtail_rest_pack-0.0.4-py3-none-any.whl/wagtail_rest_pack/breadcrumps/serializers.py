from rest_framework.serializers import Field
from wagtail.core.models import Page


class BreadcrumpSerializer(Field):
    def get_parent_or_none(self, page) -> Page or None:
        result = page.get_parent()
        if result.url == '/':
            return None
        return result

    def to_representation(self, page: Page):
        parent = self.get_parent_or_none(page)
        while parent is not None:
            yield {
                'id': parent.id,
                'url': parent.url,
                'slug': parent.slug,
                'title': parent.title
            }
            parent = self.get_parent_or_none(parent)
