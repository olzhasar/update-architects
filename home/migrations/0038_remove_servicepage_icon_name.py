# Generated by Django 2.0.9 on 2019-07-21 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0037_auto_20190721_0830"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servicepage",
            name="icon_name",
        ),
    ]
