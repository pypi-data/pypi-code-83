from bakery.views import BuildableListView, BuildableTemplateView
from robots.views import RuleList
from wagtail.contrib.sitemaps.views import sitemap


class SitemapTemplateView(BuildableTemplateView):
    build_path = 'sitemap.xml'
    template_path = 'sitemap.xml'

    def get(self, request, *args, **kwargs):
        self.context = self.get_context_data(**kwargs)
        return sitemap(self.request)


class RobotsListView(RuleList, BuildableListView):
    build_path = 'robots.txt'
    template_path = 'robots.txt'

    def get(self, request, *args, **kwargs):
        self.current_site = self.get_current_site(request)
        res = super().get(request, *args, **kwargs)
        return res
