# Generated by Django 3.1.6 on 2021-04-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmspublications', '0010_auto_20210415_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='name',
            field=models.CharField(default='publication name', max_length=256),
            preserve_default=False,
        ),
    ]
