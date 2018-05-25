from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock

from home.models import RegularPage


class PortfolioIndex(RegularPage):
    parent_page_types = ['home.HomePage']
    subpage_types = ['portfolio.Project']

    content_panels = RegularPage.content_panels + [
        InlinePanel('categories', label='Portfolio Categories')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['projects'] = Project.objects.live()
        return context


class ProjectCategory(Orderable):
    page = ParentalKey(PortfolioIndex, on_delete=models.CASCADE,
                       related_name='categories')
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name')
    ]


class Project(Page):
    parent_page_types = ['portfolio.Portfolio']
    subpage_types = []
