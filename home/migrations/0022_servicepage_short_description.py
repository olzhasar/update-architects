# Generated by Django 2.0.5 on 2018-05-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0021_auto_20180525_1102"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicepage",
            name="short_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
