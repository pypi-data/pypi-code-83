import pytz

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_minute_step(value):
    if not value or 60 % value:
        raise ValidationError(_('The value must be a divisor of 60.'))


class Schedule(models.Model):
    TZ_CHOICES = ((i, i) for i in pytz.all_timezones)

    name = models.CharField(_('name'), max_length=80, unique=True)
    minute_step = models.PositiveSmallIntegerField(
        _('minute step'),
        validators=[MinValueValidator(1), MaxValueValidator(60),
                    validate_minute_step]
    )
    tz = models.CharField(_('timezone'), max_length=80, choices=TZ_CHOICES)
    properties = models.TextField(_('properties'), blank=True)

    class Meta:
        app_label = 'task_schedule'
        ordering = ['name']
        verbose_name = _('schedule')
        verbose_name_plural = _('schedules')

    def __str__(self):
        return self.name

    def clean(self):
        tasks = Task.objects.filter(column__schedule=self)
        for task in tasks:
            if (task.minute % self.minute_step or
                    task.duration % self.minute_step):
                raise ValidationError(
                    _('Tasks fields are not multiples of the minute step.')
                )


class Column(models.Model):
    name = models.CharField(_('name'), max_length=80)
    sort = models.IntegerField(_('sort'), default=100)
    properties = models.TextField(_('properties'), blank=True)
    schedule = models.ForeignKey(
        Schedule, on_delete=models.PROTECT,
        verbose_name=_('schedule'),
        related_name='columns'
    )

    class Meta:
        app_label = 'task_schedule'
        ordering = ['sort', 'name']
        verbose_name = _('column')
        verbose_name_plural = _('columns')

    def __str__(self):
        return '{} ({})'.format(self.name, self.schedule_id)

    def clean(self):
        tasks = Task.objects.filter(column=self)
        if not self.schedule_id:
            return
        for task in tasks:
            if (task.minute % self.schedule.minute_step or
                    task.duration % self.schedule.minute_step):
                raise ValidationError(
                    _('Tasks fields are not multiples of the minute step.')
                )


class Task(models.Model):
    name = models.CharField(_('name'), max_length=255)
    properties = models.TextField(_('properties'), blank=True)
    hour = models.PositiveSmallIntegerField(
        _('hour'),
        validators=[MinValueValidator(0), MaxValueValidator(23)]
    )
    minute = models.PositiveSmallIntegerField(
        _('minute'),
        validators=[MinValueValidator(0), MaxValueValidator(59)]
    )
    duration = models.PositiveSmallIntegerField(
        _('duration'),
        help_text=_('Duration in minutes.'),
        validators=[MinValueValidator(1), MaxValueValidator(1440)]
    )
    column = models.ForeignKey(
        Column, on_delete=models.PROTECT,
        verbose_name=_('column'),
        related_name='tasks'
    )

    class Meta:
        app_label = 'task_schedule'
        ordering = ['hour', 'minute', 'name']
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __str__(self):
        return self.name

    def clean(self):
        if self.duration is None or not self.column_id:
            return
        if self.duration % self.column.schedule.minute_step:
            raise ValidationError(
                _('Task duration is not multiple of the schedule minute step.')
            )

        if self.minute is None:
            return
        if self.minute % self.column.schedule.minute_step:
            raise ValidationError(
                _('Start minute is not multiple of the schedule minute step.')
            )

        if self.hour is None:
            return
        if self.hour * 60 + self.minute + self.duration > 1440:
            raise ValidationError(
                _('End of task time exceeds max value.')
            )
