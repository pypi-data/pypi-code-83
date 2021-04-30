from django.conf import settings

TASK_SCHEDULE_FRONTEND = getattr(settings, 'TASK_SCHEDULE_FRONTEND', True)
