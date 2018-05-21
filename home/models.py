from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):

    body = StreamField([
        ('main_slider', blocks.ListBlock(
           blocks.StructBlock([
               ('image', ImageChooserBlock()),
               ('title', blocks.CharBlock(required=False)),
           ], icon='image'),
        )),
        ('about_block', blocks.StructBlock([
            ('header_text', blocks.CharBlock()),
            ('left_column', blocks.RichTextBlock()),
            ('right_column', blocks.RichTextBlock()),
        ])),
        ('customers', blocks.ListBlock(
            blocks.StructBlock([
                ('name', blocks.CharBlock()),
                ('logo', ImageChooserBlock()),
            ])
        )),
        ('blog_posts', blocks.StaticBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class AboutPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []


class ServicePage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []


class JobPostings(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []


class Contacts(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []
