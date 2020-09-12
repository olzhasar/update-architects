from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel

from home.models import RegularPage


class PortfolioIndex(RegularPage):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["portfolio.Project"]

    content_panels = RegularPage.content_panels + [
        InlinePanel("categories", label="Project Categories")
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context["projects"] = Project.objects.live()
        return context


class ProjectCategory(Orderable):
    page = ParentalKey(
        PortfolioIndex, on_delete=models.CASCADE, related_name="categories"
    )
    name_ru = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=100, unique=True)

    panels = [
        FieldPanel("name_ru"),
        FieldPanel("code"),
    ]

    def __str__(self):
        return self.name


class Project(Page):
    order = models.SmallIntegerField(default=0)
    subtitle_ru = models.CharField(max_length=255, blank=True, null=True)
    categories = ParentalManyToManyField(ProjectCategory, blank=True)
    year = models.IntegerField(blank=True, null=True)
    location_ru = models.CharField(max_length=255, blank=True, null=True)
    area_size_ru = models.CharField(max_length=255, blank=True, null=True)
    authors_ru = models.CharField(max_length=255, blank=True, null=True)
    status_ru = models.CharField(max_length=255, blank=True, null=True)

    description_ru = RichTextField(blank=True, null=True)

    body = None

    content_panels = Page.content_panels + [
        FieldPanel("subtitle_ru"),
        FieldPanel("categories"),
        MultiFieldPanel(
            [
                FieldPanel("year"),
                FieldPanel("location_ru"),
                FieldPanel("area_size_ru"),
                FieldPanel("authors_ru"),
                FieldPanel("status_ru"),
            ],
            heading="Project details",
        ),
        FieldPanel("description_ru"),
        InlinePanel("images", label="Project images"),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel("order"),
    ]

    parent_page_types = ["portfolio.PortfolioIndex"]
    subpage_types = []

    def get_sitemap_urls(self):
        return [
            {
                "location": self.full_url,
                "lastmod": self.latest_revision_created_at,
                "changefreq": "weekly",
                "priority": 0.64,
            }
        ]


class ProjectImage(Orderable):
    page = ParentalKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    SIZES = (
        (12, "Full width"),
        (6, "Half"),
        (4, "One-third"),
    )
    size = models.PositiveSmallIntegerField(choices=SIZES, default=12)

    panels = [ImageChooserPanel("image"), FieldPanel("size")]
