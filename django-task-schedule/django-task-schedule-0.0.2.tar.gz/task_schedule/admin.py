from django.contrib import admin

from task_schedule.models import Schedule, Column, Task


class ColumnInline(admin.TabularInline):
    model = Column


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'minute_step', 'tz', 'properties')
    inlines = [ColumnInline]


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'properties', 'schedule')
    list_select_related = ('schedule',)
    list_filter = ('schedule',)
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'hour', 'minute', 'duration', 'properties',
                    'column')
    list_select_related = ('column',)
    list_filter = ('column', 'column__schedule')
