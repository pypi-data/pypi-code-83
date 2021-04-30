from django.urls import path, include, re_path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter

from task_schedule import views
from task_schedule import settings

app_name = 'task_schedule'

router = SimpleRouter(trailing_slash=False)
router.register(r'schedules', views.ScheduleViewSet)
router.register(r'columns', views.ColumnViewSet)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = format_suffix_patterns([
    path(r'permissions', views.PermissionsView.as_view()),
    path('', include(router.urls)),
])

if settings.TASK_SCHEDULE_FRONTEND:
    urlpatterns += [
        path(r'', views.index, name='index'),
        re_path(r'^(?P<path>.*)/$', views.index, name='index')
    ]
