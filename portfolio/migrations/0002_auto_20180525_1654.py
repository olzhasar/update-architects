# Generated by Django 2.0.5 on 2018-05-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectcategory",
            name="code",
            field=models.CharField(default="", max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="projectcategory",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
