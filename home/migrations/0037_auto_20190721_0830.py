# Generated by Django 2.0.9 on 2019-07-21 08:30

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0036_auto_20190721_0718"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                (
                    (
                        "main_banner",
                        wagtail.core.blocks.StructBlock(
                            (
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("title", wagtail.core.blocks.CharBlock()),
                                (
                                    "subtitle",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                            ),
                            template="home/blocks/main_banner.html",
                        ),
                    ),
                    (
                        "about_block",
                        wagtail.core.blocks.StructBlock(
                            (
                                ("title", wagtail.core.blocks.CharBlock()),
                                ("header_text", wagtail.core.blocks.CharBlock()),
                                ("left_column", wagtail.core.blocks.RichTextBlock()),
                                ("right_column", wagtail.core.blocks.RichTextBlock()),
                            ),
                            template="home/blocks/about_block.html",
                        ),
                    ),
                    (
                        "portfolio_block",
                        wagtail.core.blocks.StructBlock(
                            (
                                ("title", wagtail.core.blocks.CharBlock()),
                                ("subtitle", wagtail.core.blocks.CharBlock()),
                                (
                                    "projects",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.PageChooserBlock(
                                            target_model=["portfolio.Project"]
                                        )
                                    ),
                                ),
                                (
                                    "portfolio_link",
                                    wagtail.core.blocks.URLBlock(required=False),
                                ),
                            ),
                            template="home/blocks/portfolio_block.html",
                        ),
                    ),
                    (
                        "customers",
                        wagtail.core.blocks.ListBlock(
                            wagtail.core.blocks.StructBlock(
                                (
                                    ("name", wagtail.core.blocks.CharBlock()),
                                    ("logo", wagtail.images.blocks.ImageChooserBlock()),
                                ),
                                icon="group",
                            ),
                            template="home/blocks/customers.html",
                        ),
                    ),
                )
            ),
        ),
    ]
