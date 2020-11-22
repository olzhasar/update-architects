from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmenus.models import AbstractMainMenuItem

from core.mixins import TranslatedMixin


class CustomMainMenuItem(TranslatedMixin, AbstractMainMenuItem):
    """A custom menu item model to be used by ``wagtailmenus.MainMenu``"""

    menu = ParentalKey(
        "wagtailmenus.MainMenu",
        on_delete=models.CASCADE,
        related_name="custom_menu_items",  # important for step 3!
    )
    link_text_en = models.CharField(max_length=250, blank=True)

    # Also override the panels attribute, so that the new fields appear
    # in the admin interface
    panels = (
        PageChooserPanel("link_page"),
        FieldPanel("link_url"),
        FieldPanel("url_append"),
        FieldPanel("link_text"),
        FieldPanel("link_text_en"),
        FieldPanel("allow_subnav"),
    )
