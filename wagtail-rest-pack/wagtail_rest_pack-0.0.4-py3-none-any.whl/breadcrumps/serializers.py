from rest_framework.serializers import Field
from wagtail.core.models import Page


class BreadcrumpSerializer(Field):
    def get_parent_or_none(self, page) -> Page or None:
        if page.url == '/':
            return None
        return page.get_parent()

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
