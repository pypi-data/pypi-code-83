# Generated by Django 2.0.7 on 2018-09-21 14:32

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foo',
            name='geo_collection',
            field=django.contrib.gis.db.models.fields.GeometryCollectionField(default=None, srid=4326),
            preserve_default=False,
        ),
    ]
