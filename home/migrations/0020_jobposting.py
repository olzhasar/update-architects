# Generated by Django 2.0.5 on 2018-05-25 11:00

import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0019_auto_20180525_0912"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobPosting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("content", wagtail.core.fields.RichTextField()),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="postings",
                        to="home.JobPostings",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
