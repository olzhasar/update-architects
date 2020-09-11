# Generated by Django 2.0.5 on 2018-05-23 09:40

import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_auto_20180523_0929"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                (
                    (
                        "main_slider",
                        wagtail.core.blocks.ListBlock(
                            wagtail.core.blocks.StructBlock(
                                (
                                    (
                                        "image",
                                        wagtail.images.blocks.ImageChooserBlock(),
                                    ),
                                    (
                                        "title",
                                        wagtail.core.blocks.CharBlock(required=False),
                                    ),
                                    (
                                        "subtitle",
                                        wagtail.core.blocks.CharBlock(required=False),
                                    ),
                                    (
                                        "button_text",
                                        wagtail.core.blocks.CharBlock(required=False),
                                    ),
                                    (
                                        "button_link",
                                        wagtail.core.blocks.URLBlock(required=False),
                                    ),
                                ),
                                icon="image",
                            ),
                            template="home/blocks/main_slider.html",
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
                        "customers",
                        wagtail.core.blocks.ListBlock(
                            wagtail.core.blocks.StructBlock(
                                (
                                    ("name", wagtail.core.blocks.CharBlock()),
                                    ("logo", wagtail.images.blocks.ImageChooserBlock()),
                                )
                            ),
                            template="home/blocks/customers.html",
                        ),
                    ),
                    (
                        "blog_posts",
                        wagtail.core.blocks.static_block.StaticBlock(
                            template="home/blocks/blog_posts.html"
                        ),
                    ),
                )
            ),
        ),
    ]
