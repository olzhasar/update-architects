from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class Portfolio(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['portfolio.Project']


class Project(Page):
    parent_page_types = ['portfolio.Portfolio']
    subpage_types = []
