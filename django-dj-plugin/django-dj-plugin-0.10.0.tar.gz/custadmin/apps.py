from django.contrib.admin.apps import apps


class MyAdminConfig(apps.AdminConfig):
    default_site = 'custadmin.admin.MyAdminSite'
