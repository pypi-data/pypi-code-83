from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from task_schedule.models import Schedule, Column, Task


class ScheduleSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ['id', 'name', 'minute_step', 'tz', 'properties', 'data']
        read_only_fields = ['data']

    def get_data(self, obj):
        if self.context['view'].action != 'retrieve':
            return

        data = {'columns': []}
        for column in obj.columns.all():
            column_data = {
                'id': column.id,
                'name': column.name,
                'sort': column.sort,
                'tasks': []
            }
            for task in column.tasks.all():
                task = {
                    'id': task.id,
                    'name': task.name,
                    'hour': task.hour,
                    'minute': task.minute,
                    'duration': task.duration
                }
                column_data['tasks'].append(task)
            data['columns'].append(column_data)

        return data

    def validate(self, data):
        minute_step = data.get('minute_step')
        if minute_step:
            self._validate_minute_step(minute_step)

        return data

    def _validate_minute_step(self, minute_step):
        tasks = Task.objects.filter(column__schedule=self.instance)
        for task in tasks:
            if task.minute % minute_step or task.duration % minute_step:
                raise ValidationError(
                    _('Tasks fields are not multiples of the minute step.')
                )


class ColumnSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = Column
        fields = ['id', 'name', 'sort', 'schedule', 'properties', 'data']
        read_only_fields = ['data']

    def get_data(self, obj):
        if self.context['view'].action != 'retrieve':
            return

        data = {'tasks': []}
        for task in obj.tasks.all():
            data['tasks'].append({
                'id': task.id,
                'name': task.name,
                'hour': task.hour,
                'minute': task.minute,
                'duration': task.duration
            })

        return data

    def validate(self, data):
        schedule = data.get('schedule')
        if self.instance and schedule:
            self._validate_schedule(schedule.minute_step)

        return data

    def _validate_schedule(self, minute_step):
        tasks = Task.objects.filter(column=self.instance)
        for task in tasks:
            if task.minute % minute_step or task.duration % minute_step:
                raise ValidationError(
                    _('Tasks fields are not multiples of the minute step.')
                )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'hour', 'minute', 'duration', 'properties',
                  'column']

    def validate(self, data):
        column = data.get('column') or self.instance.column

        duration = data.get('duration')
        if duration:
            self._validate_duration(duration, column)

        minute = data.get('minute')
        if minute:
            self._validate_minute(minute, column)

        hour = data.get('hour')
        if duration or minute or hour:
            self._validate_end_time(data)

        return data

    @staticmethod
    def _validate_duration(duration, column):
        if duration % column.schedule.minute_step:
            raise ValidationError(
                _('Task duration is not multiple of the schedule minute step.')
            )

    @staticmethod
    def _validate_minute(minute, column):
        if minute % column.schedule.minute_step:
            raise ValidationError(
                _('Start minute is not multiple of the schedule minute step.')
            )

    def _validate_end_time(self, data):
        hour = data.get('hour')
        if hour is None:
            hour = self.instance.hour
        minute = data.get('minute')
        if minute is None:
            minute = self.instance.minute
        duration = data.get('duration') or self.instance.duration
        if hour * 60 + minute + duration > 1440:
            raise ValidationError(
                _('End of task time exceeds max value.')
            )
