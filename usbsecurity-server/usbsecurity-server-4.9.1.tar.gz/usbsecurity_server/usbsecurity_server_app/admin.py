#  This module belongs to the usbsecurity-server project.
#  Copyright (c) 2021 Alexis Torres Valdes
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Contact: alexis89.dev@gmail.com

from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from usbsecurity_server.usbsecurity_server_app.forms import DeviceAdminForm
from usbsecurity_server.usbsecurity_server_app.models import DeviceType, AccountSession, AccountDevice, AccountComputer, Account, Device, \
    Computer, DeviceModel, DeviceBrand


admin.site.site_header = _('Manage USBSecurity')
admin.site.site_title = _('USBSecurity administration')
admin.site.index_title = _('Welcome to USBSecurity administration')


admin.site.unregister(User)


@admin.register(User)
class MyUserAdmin(UserAdmin):
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        if request.user.is_superuser:
            perm_fields = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        else:
            perm_fields = ('is_active', 'is_staff')

        return [(None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': perm_fields}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')})]

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_superuser=False)
        return qs


class BaseAdmin(admin.ModelAdmin):
    @staticmethod
    def get_fields_exclude(fields, excludes):
        _fields = []
        for field in fields:
            if field not in excludes:
                _fields.append(field)
        return _fields

    @staticmethod
    def insert_fields(fields, fields_base, index):
        union = fields_base[:index] + fields + fields_base[index:]
        return union

    fieldsets = [
        [
            'Admin',
            {'fields': ['_comment']}
        ],
        [
            'Date Time',
            {'fields': ['date_time_created', 'date_time_modified']}
        ],
    ]
    readonly_fields = ['id', 'date_time_created', 'date_time_modified']
    ordering = ['-date_time_modified']
    list_display = ['id', 'date_time_created', 'date_time_modified']
    list_per_page = 100

    fieldsets_index_insert = 0
    list_display_index_insert = 0


@admin.register(DeviceType)
class DeviceTypeAdmin(BaseAdmin):
    _fieldsets = [
        [
            None,
            {'fields': ['name']}
        ],
    ]
    _list_display = ['name']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    search_fields = ['name']
    list_display_links = ['name']


@admin.register(DeviceBrand)
class DeviceBrandAdmin(BaseAdmin):
    _fieldsets = [
        [
            None,
            {'fields': ['type', 'name']}
        ],
    ]
    _list_display = ['type', 'name']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    search_fields = ['type', 'name']
    list_display_links = ['name']


@admin.register(DeviceModel)
class DeviceModelAdmin(BaseAdmin):
    _fieldsets = [
        [
            None,
            {'fields': ['brand', 'name']}
        ],
    ]
    _list_display = ['brand', 'name']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    search_fields = ['brand', 'name']
    list_display_links = ['name']


@admin.register(Computer)
class ComputerAdmin(BaseAdmin):
    _fieldsets = [
        [
            None,
            {'fields': ['ip_address']}
        ],
    ]
    _list_display = ['ip_address']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    search_fields = ['ip_address']
    list_display_links = ['ip_address']


@admin.register(Device)
class DeviceAdmin(BaseAdmin):
    form = DeviceAdminForm

    _fieldsets = [
        [
            None,
            {'fields': ['ls_id', 'model', 'identifier']}
        ],
    ]
    _list_display = ['ls_id', 'model', 'identifier']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    search_fields = ['ls_id', 'identifier']
    list_display_links = ['ls_id']


@admin.register(Account)
class AccountAdmin(BaseAdmin):
    _fieldsets = [
        [
            None,
            {'fields': ['user', 'is_for_all']}
        ],
    ]
    _list_display = ['user', 'is_for_all']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    list_filter = ['is_for_all']
    list_display_links = ['user']


@admin.register(AccountComputer)
class AccountComputerAdmin(BaseAdmin):
    _fieldsets = [
        [
            None,
            {'fields': ['account', 'computer']}
        ],
    ]
    _list_display = ['account', 'computer']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    list_display_links = ['account']


@admin.register(AccountDevice)
class AccountDeviceAdmin(BaseAdmin):
    _fieldsets = [
        [
            None,
            {'fields': ['account', 'device']}
        ],
    ]
    _list_display = ['account', 'device']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    list_display_links = ['account']


@admin.register(AccountSession)
class AccountSessionAdmin(BaseAdmin):
    _fieldsets = [
        [
            None,
            {'fields': ['account', 'ip_address', 'is_closed']}
        ],
    ]
    _list_display = ['account', 'ip_address', 'is_closed']

    fieldsets = BaseAdmin.insert_fields(_fieldsets, BaseAdmin.fieldsets, BaseAdmin.fieldsets_index_insert)
    list_display = BaseAdmin.insert_fields(_list_display, BaseAdmin.list_display, BaseAdmin.list_display_index_insert)
    search_fields = ['ip_address']
    list_filter = ['is_closed']
    list_display_links = ['account']
    actions = ['close_all']

    # def has_add_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False

    def close_all(self, request, queryset):
        objs = []
        for obj in queryset:
            obj.is_closed = True
            objs.append(obj)
        AccountSession.objects.bulk_update(objs, ['is_closed'])
        closed_all = not AccountSession.objects.filter(is_closed=False).exists()
        if not closed_all:
            self.message_user(request, 'No todas las sesiones han sido cerradas', messages.WARNING)
        else:
            self.message_user(request, 'Todas las sesiones han sido cerradas', messages.SUCCESS)

    close_all.short_description = "Cerrar todas las sesiones"
