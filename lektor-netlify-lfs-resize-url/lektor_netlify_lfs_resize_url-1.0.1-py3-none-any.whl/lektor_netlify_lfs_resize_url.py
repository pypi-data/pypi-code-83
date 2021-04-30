# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


def nf_resize(source: str, nf_resize='fit', h='', w='') -> str:
    if nf_resize == 'fit' or nf_resize == 'smartcrop':
        if h or w:
            source += f'?nf_resize={nf_resize}'

        if h:
            source += f'&h={str(h)}'

        if w:
            source += f'&w={str(w)}'
    return source


class NetlifyLfsResizeUrlPlugin(Plugin):
    name = 'netlify-lfs-resize-url'
    description = u'Convert image URLs to Netlify LFS resize URLs.'

    def on_process_template_context(self, context, **extra):
        def test_function():
            return f'Value from plugin {self.name}'
        context['test_function'] = test_function

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['nf_resize'] = nf_resize
        # self.env.jinja_env.globals.update(nf_resize=nf_resize)
