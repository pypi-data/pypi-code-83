# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-13 08:19
from __future__ import unicode_literals

import timezone_field.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("periodic_task", "0002_auto_20190103_1918"),
    ]

    operations = [
        migrations.AddField(
            model_name="periodictask",
            name="priority",
            field=models.IntegerField(default=100, verbose_name="流程优先级"),
        ),
        migrations.AddField(
            model_name="periodictask",
            name="queue",
            field=models.CharField(default="", max_length=512, verbose_name="流程使用的队列名"),
        ),
        migrations.AlterField(
            model_name="crontabschedule",
            name="day_of_month",
            field=models.CharField(
                default="*", max_length=64, verbose_name="day of month"
            ),
        ),
        migrations.AlterField(
            model_name="crontabschedule",
            name="day_of_week",
            field=models.CharField(
                default="*", max_length=64, verbose_name="day of week"
            ),
        ),
        migrations.AlterField(
            model_name="crontabschedule",
            name="hour",
            field=models.CharField(default="*", max_length=64, verbose_name="hour"),
        ),
        migrations.AlterField(
            model_name="crontabschedule",
            name="minute",
            field=models.CharField(default="*", max_length=64, verbose_name="minute"),
        ),
        migrations.AlterField(
            model_name="crontabschedule",
            name="month_of_year",
            field=models.CharField(
                default="*", max_length=64, verbose_name="month of year"
            ),
        ),
        migrations.AlterField(
            model_name="crontabschedule",
            name="timezone",
            field=timezone_field.fields.TimeZoneField(default="UTC"),
        ),
        migrations.AlterField(
            model_name="djceleryperiodictask",
            name="args",
            field=models.TextField(
                blank=True,
                default="[]",
                help_text="JSON encoded positional arguments",
                verbose_name="Arguments",
            ),
        ),
        migrations.AlterField(
            model_name="djceleryperiodictask",
            name="kwargs",
            field=models.TextField(
                blank=True,
                default="{}",
                help_text="JSON encoded keyword arguments",
                verbose_name="Keyword arguments",
            ),
        ),
        migrations.AlterField(
            model_name="intervalschedule",
            name="period",
            field=models.CharField(
                choices=[
                    ("days", "Days"),
                    ("hours", "Hours"),
                    ("minutes", "Minutes"),
                    ("seconds", "Seconds"),
                    ("microseconds", "Microseconds"),
                ],
                max_length=24,
                verbose_name="period",
            ),
        ),
        migrations.AlterField(
            model_name="periodictask",
            name="creator",
            field=models.CharField(default="", max_length=32, verbose_name="创建者"),
        ),
    ]
