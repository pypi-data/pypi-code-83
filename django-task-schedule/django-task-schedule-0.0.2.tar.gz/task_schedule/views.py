from django.db.models import ProtectedError
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet as ModelViewSetBase

from task_schedule.models import Schedule, Column, Task
from task_schedule.serializers import (
    ScheduleSerializer,
    ColumnSerializer,
    TaskSerializer,
)


def index(request, path=''):
    return render(request, 'task_schedule/index.html')


class ModelViewSet(ModelViewSetBase):
    protected_message = ''

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError:
            raise ValidationError({
                "non_field_errors": [self.protected_message]
            })


class PermissionsView(APIView):
    def get(self, request):
        return Response(
            [i[14:] for i in self.request.user.get_all_permissions()
             if i.startswith('task_schedule.')]
        )


class ScheduleViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Schedule.objects.prefetch_related(
        'columns', 'columns__tasks'
    ).all()
    serializer_class = ScheduleSerializer

    protected_message = _('Schedule has dependent columns.')


class ColumnViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    protected_message = _('Column has dependent tasks.')


class TaskViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
