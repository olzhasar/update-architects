from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         StreamFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel

from home.models import RegularPage


class PortfolioIndex(RegularPage):
    parent_page_types = ['home.HomePage']
    subpage_types = ['portfolio.Project']

    content_panels = RegularPage.content_panels + [
        InlinePanel('categories', label='Project Categories')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['projects'] = Project.objects.live()
        return context


class ProjectCategory(Orderable):
    page = ParentalKey(PortfolioIndex, on_delete=models.CASCADE,
                       related_name='categories')
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=100, unique=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('code'),
    ]

    def __str__(self):
        return self.name


class Project(Page):
    categories = ParentalManyToManyField(ProjectCategory,
                                         blank=True, null=True)

    body = StreamField([
        ('project_details', blocks.StructBlock([
            ('Date', blocks.CharBlock()),
            ('Client', blocks.CharBlock()),
        ])),
        ('project_description', blocks.StructBlock([
            ('left_column', blocks.RichTextBlock()),
            ('right_column', blocks.RichTextBlock()),
        ])),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('categories'),
        InlinePanel('images', label='Project images'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['portfolio.PortfolioIndex']
    subpage_types = []


class ProjectImage(Orderable):
    page = ParentalKey(Project, on_delete=models.CASCADE,
                       related_name='images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image')
    ]
