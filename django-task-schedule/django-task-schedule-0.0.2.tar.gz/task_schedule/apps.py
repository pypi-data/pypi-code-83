from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TaskScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_schedule'
    verbose_name = _('Task Schedule')
