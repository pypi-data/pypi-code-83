# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-21 15:20


from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20170620_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='time_of_delivery',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Holds the date and time the Delivery was uploaded.', verbose_name='Time of delivery'),
        ),
        migrations.AlterField(
            model_name='groupinvite',
            name='sent_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
