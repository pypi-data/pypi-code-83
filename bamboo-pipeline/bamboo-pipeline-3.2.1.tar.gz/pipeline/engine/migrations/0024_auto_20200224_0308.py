# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-24 03:08
from __future__ import unicode_literals

from django.db import migrations

import pipeline.engine.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0023_status_state_refresh_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="ex_data",
            field=pipeline.engine.models.fields.IOField(default=None, verbose_name="异常数据"),
        ),
        migrations.AlterField(
            model_name="data",
            name="inputs",
            field=pipeline.engine.models.fields.IOField(default=None, verbose_name="输入数据"),
        ),
        migrations.AlterField(
            model_name="data",
            name="outputs",
            field=pipeline.engine.models.fields.IOField(default=None, verbose_name="输出数据"),
        ),
        migrations.AlterField(
            model_name="historydata",
            name="ex_data",
            field=pipeline.engine.models.fields.IOField(default=None, verbose_name="异常数据"),
        ),
        migrations.AlterField(
            model_name="historydata",
            name="inputs",
            field=pipeline.engine.models.fields.IOField(default=None, verbose_name="输入数据"),
        ),
        migrations.AlterField(
            model_name="historydata",
            name="outputs",
            field=pipeline.engine.models.fields.IOField(default=None, verbose_name="输出数据"),
        ),
    ]
