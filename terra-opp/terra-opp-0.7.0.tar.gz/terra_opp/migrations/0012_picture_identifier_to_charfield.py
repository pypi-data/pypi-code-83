# Generated by Django 3.2 on 2021-04-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("terra_opp", "0011_auto_20210412_1000"),
    ]

    operations = [
        migrations.RenameField(
            model_name="picture",
            old_name="identifier",
            new_name="old_identifier",
        ),
        migrations.AddField(
            model_name="picture",
            name="identifier",
            field=models.CharField(
                default="", max_length=10, verbose_name="Identifier"
            ),
        ),
    ]
