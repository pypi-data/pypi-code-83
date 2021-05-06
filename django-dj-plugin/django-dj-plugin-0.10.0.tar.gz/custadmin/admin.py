from django.apps import apps
from django.contrib.admin import AdminSite
from django.http import Http404
from django.template.response import TemplateResponse
from django.urls import reverse, NoReverseMatch
from django.utils.text import capfirst
from django.utils.translation import gettext as _


class MyAdminSite(AdminSite):

    def _build_app_dict(self, request, label=None):
        user = request.user
        app_dict = {}

        if label:
            models = {
                m: m_a for m, m_a in self._registry.items()
                if m._meta.app_label == label
            }
        else:
            models = self._registry

        for model, model_admin in models.items():
            app_label = model._meta.app_label
            # 是否隐藏菜单
            if not user.is_superuser and hasattr(model_admin, 'menu_hidden'):
                menu_hidden = model_admin.menu_hidden
                if menu_hidden:
                    continue

            # 排序
            name = capfirst(model._meta.verbose_name_plural)
            menu_index = ord(name[:1])
            if hasattr(model_admin, 'menu_index'):
                menu_index = model_admin.menu_index
                if menu_index and type(menu_index) == int:
                    menu_index = menu_index

            has_module_perms = model_admin.has_module_permission(request)
            if not has_module_perms:
                continue

            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True not in perms.values():
                continue

            info = (app_label, model._meta.model_name)
            model_dict = {
                'name': name,
                'object_name': model._meta.object_name,
                'perms': perms,
                'admin_url': None,
                'add_url': None,
                'menu_index': menu_index,
            }
            if perms.get('change') or perms.get('view'):
                model_dict['view_only'] = not perms.get('change')
                try:
                    model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=self.name)
                except NoReverseMatch:
                    pass
            if perms.get('add'):
                try:
                    model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=self.name)
                except NoReverseMatch:
                    pass

            if app_label in app_dict:
                app_dict[app_label]['models'].append(model_dict)
            else:
                app_dict[app_label] = {
                    'name': apps.get_app_config(app_label).verbose_name,
                    'app_label': app_label,
                    'app_url': reverse(
                        'admin:app_list',
                        kwargs={'app_label': app_label},
                        current_app=self.name,
                    ),
                    'has_module_perms': has_module_perms,
                    'models': [model_dict],
                }

        if label:
            return app_dict.get(label)
        return app_dict

    def app_index(self, request, app_label, extra_context=None):
        app_dict = self._build_app_dict(request, app_label)
        if not app_dict:
            raise Http404('The requested admin page does not exist.')
        # Sort the models alphabetically within each app.
        app_dict['models'].sort(key=lambda x: x['menu_index'])
        app_name = apps.get_app_config(app_label).verbose_name
        context = {
            **self.each_context(request),
            'title': _('%(app)s administration') % {'app': app_name},
            'app_list': [app_dict],
            'app_label': app_label,
            **(extra_context or {}),
        }

        request.current_app = self.name

        return TemplateResponse(request, self.app_index_template or [
            'admin/%s/app_index.html' % app_label,
            'admin/app_index.html'
        ], context)

    def get_app_list(self, request):
        user = request.user
        groups = user.groups.filter()

        app_dict = self._build_app_dict(request)
        is_installed = apps.is_installed('custmenu')

        if is_installed:
            from custmenu.models import MinorAddress
            from custmenu.utils import add_menu_to_app_list

            if user.is_superuser or groups:
                addresses = MinorAddress.objects.filter(menu_hidden=False, major__menu_hidden=False)
                for address in addresses:
                    if user.is_superuser or address.group in groups:
                        add_menu_to_app_list(app_dict, address)

        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        for app in app_list:
            app['models'].sort(key=lambda x: x['menu_index'])

        return app_list
