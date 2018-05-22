# Generated by Django 2.0.5 on 2018-05-22 14:52

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_aboutpage_contacts_jobpostings_servicepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('main_slider', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False))), icon='image', template='partials/main_slider.html'))), ('about_block', wagtail.core.blocks.StructBlock((('header_text', wagtail.core.blocks.CharBlock()), ('left_column', wagtail.core.blocks.RichTextBlock()), ('right_column', wagtail.core.blocks.RichTextBlock())))), ('customers', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock()), ('logo', wagtail.images.blocks.ImageChooserBlock()))))), ('blog_posts', wagtail.core.blocks.static_block.StaticBlock()))),
        ),
    ]
