from rest_framework import mixins, permissions, viewsets

from huscy.data_protection.serializer import DataRequestSerializer
from huscy.subjects.models import Subject


class SubjectViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Subject.objects.all()
    serializer_class = DataRequestSerializer
