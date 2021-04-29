from django.contrib import admin

from huscy.attributes import models


class AttributeSchemaAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.AttributeSchema, AttributeSchemaAdmin)
