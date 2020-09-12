from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

from .translations import TranslationProxy


class TranslatedMixin:
    translated = TranslationProxy()


class TranslatedPageMixin(models.Model):
    title_en = models.CharField(
        verbose_name=_("title en"),
        max_length=255,
        help_text=_("The page title as you'd like it to be seen by the public"),
        null=True,
    )

    seo_title_en = models.CharField(
        verbose_name=_("page title en"),
        max_length=255,
        blank=True,
        help_text=_(
            "Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window."
        ),
    )
    search_description_en = models.TextField(
        verbose_name=_("search description en"), blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("title_en"),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel("seo_title_en"),
        FieldPanel("search_description_en"),
    ]
    translated = TranslationProxy()

    class Meta:
        abstract = True
