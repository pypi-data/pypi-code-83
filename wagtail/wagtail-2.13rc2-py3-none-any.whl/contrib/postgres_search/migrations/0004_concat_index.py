# Generated by Django 3.1.3 on 2020-11-13 16:55

from django.db import migrations

from wagtail.contrib.postgres_search.models import IndexEntry

table = IndexEntry._meta.db_table


class Migration(migrations.Migration):

    dependencies = [
        ('postgres_search', '0003_title'),
    ]

    operations = [
        migrations.RunSQL(
            'CREATE INDEX {0}_title_body_concat_search ON {0} '
            'USING GIN(( title || body));'.format(table),
            'DROP INDEX IF EXISTS {0}_title_body_concat_search;'.format(table),
        ),
    ]
