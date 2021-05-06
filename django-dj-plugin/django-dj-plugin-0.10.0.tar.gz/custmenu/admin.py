from django.contrib import admin
from custmenu.inlines import MinorAddressInline
from custmenu.models import MinorAddress, MajorAddress


@admin.register(MajorAddress)
class MajorAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'app_label', 'app_url', 'menu_hidden', 'created', 'modified')
    list_display_links = ('id', 'name', 'app_label', 'app_url', )
    inlines = (MinorAddressInline, )


@admin.register(MinorAddress)
class MajorAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'major', 'name', 'object_name', 'menu_hidden', 'menu_index', 'group', 'created', 'modified')
    list_display_links = ('id', 'major', 'name', 'object_name', )
    list_filter = ('major', 'menu_hidden', )
