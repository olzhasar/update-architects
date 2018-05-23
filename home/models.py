from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):

    body = StreamField([
        ('main_slider', blocks.ListBlock(
           blocks.StructBlock([
               ('image', ImageChooserBlock()),
               ('title', blocks.CharBlock(required=False)),
               ('subtitle', blocks.CharBlock(required=False)),
               ('button_text', blocks.CharBlock(required=False)),
               ('button_link', blocks.URLBlock(required=False)),
           ], icon='image'),
           template='home/blocks/main_slider.html'
        )),
        ('about_block', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('header_text', blocks.CharBlock()),
            ('left_column', blocks.RichTextBlock()),
            ('right_column', blocks.RichTextBlock()),
        ], template='home/blocks/about_block.html')),
        ('customers', blocks.ListBlock(
            blocks.StructBlock([
                ('name', blocks.CharBlock()),
                ('logo', ImageChooserBlock()),
            ], icon='group'),
            template='home/blocks/customers.html'
        )),
        ('blog_posts', blocks.StaticBlock(
            template='home/blocks/blog_posts.html'
        )),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['services'] = ServicePage.objects.live()
        return context


class AboutPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []


class ServicesPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['home.ServicePage']


class ServicePage(Page):
    icon_name = models.CharField(max_length=100)
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('icon_name'),
        ImageChooserPanel('header_image'),
        FieldPanel('body', classname="full"),
    ]

    parent_page_types = ['home.ServicesPage']
    subpage_types = []


class JobPostings(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []


class Contacts(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = []
