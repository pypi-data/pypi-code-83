# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 05:51


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20180214_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='deadline_handling',
            field=models.PositiveIntegerField(choices=[(0, 'Soft deadlines'), (1, 'Hard deadlines')], default=1, help_text='With HARD deadlines, students will be unable to make deliveries when a deadline has expired. With SOFT deadlines students will be able to make deliveries after the deadline has expired. All deliveries after their deadline are clearly highligted. NOTE: Devilry is designed from the bottom up to gracefully handle SOFT deadlines. Students have to perform an extra confirm-step when adding deliveries after their active deadline, and assignments where the deadline has expired is clearly marked for both students and examiners.', verbose_name='Deadline handling'),
        ),
    ]
