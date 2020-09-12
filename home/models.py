from django.db import models
from modelcluster.fields import ParentalKey
from puput.models import EntryPage
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


class HomePage(Page):

    body_ru = StreamField(
        [
            (
                "main_banner",
                blocks.StructBlock(
                    [
                        ("image", ImageChooserBlock()),
                        ("title", blocks.CharBlock()),
                        ("subtitle", blocks.CharBlock(required=False)),
                    ],
                    template="home/blocks/main_banner.html",
                ),
            ),
            (
                "about_block",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("header_text", blocks.CharBlock()),
                        ("content", blocks.RichTextBlock()),
                    ],
                    template="home/blocks/about_block.html",
                ),
            ),
            (
                "portfolio_block",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("subtitle", blocks.CharBlock()),
                        (
                            "projects",
                            blocks.ListBlock(
                                blocks.PageChooserBlock(
                                    target_model="portfolio.project"
                                )
                            ),
                        ),
                        ("portfolio_link", blocks.URLBlock(required=False)),
                    ],
                    template="home/blocks/portfolio_block.html",
                ),
            ),
            (
                "customers",
                blocks.ListBlock(
                    blocks.StructBlock(
                        [("name", blocks.CharBlock()), ("logo", ImageChooserBlock()),],
                        icon="group",
                    ),
                    template="home/blocks/customers.html",
                ),
            ),
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body_ru"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["entries"] = EntryPage.objects.live().order_by("-date")[:3]
        return context

    def get_sitemap_urls(self):
        return [
            {
                "location": self.full_url,
                "lastmod": self.latest_revision_created_at,
                "changefreq": "weekly",
                "priority": 1.0,
            }
        ]


class RegularPage(Page):
    is_abstract = True

    subtitle_ru = models.CharField(max_length=255, blank=True, null=True)
    body_ru = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle_ru"),
        FieldPanel("body_ru", classname="full"),
    ]

    class Meta:
        abstract = True

    def get_sitemap_urls(self):
        return [
            {
                "location": self.full_url,
                "lastmod": self.latest_revision_created_at,
                "changefreq": "weekly",
                "priority": 0.8,
            }
        ]


class StandardPage(RegularPage):
    pass


class ServicesPage(RegularPage):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["home.ServicePage"]

    def get_context(self, request):
        context = super().get_context(request)
        context["services"] = ServicePage.objects.live()
        return context


class ServicePage(RegularPage):
    short_description_ru = models.TextField(blank=True, null=True)
    wiki_url = models.URLField(blank=True, null=True)

    promote_panels = RegularPage.promote_panels + [
        FieldPanel("short_description_ru"),
        FieldPanel("wiki_url"),
    ]

    parent_page_types = ["home.ServicesPage"]
    subpage_types = []


class AboutPage(RegularPage):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["home.JobPostings", "home.Contacts", "home.StandardPage"]
    content_panels = RegularPage.content_panels + [
        InlinePanel("members", label="Team members")
    ]


class TeamMember(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name="members")
    name_ru = models.CharField(max_length=255)
    job_title_ru = models.CharField(max_length=255)
    body = None
    avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name_ru"),
        FieldPanel("job_title_ru"),
        ImageChooserPanel("avatar"),
    ]


class JobPostings(RegularPage):
    content_panels = RegularPage.content_panels + [
        InlinePanel("postings", label="Job postings")
    ]
    parent_page_types = ["home.HomePage"]
    subpage_types = []


class JobPosting(Orderable):
    page = ParentalKey(JobPostings, on_delete=models.CASCADE, related_name="postings")
    job_title_ru = models.CharField(max_length=255)
    description_ru = RichTextField()

    panels = [
        FieldPanel("job_title_ru"),
        FieldPanel("description_ru", classname="full"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey("Contacts", on_delete=models.CASCADE, related_name="form_fields")


class Contacts(RegularPage, AbstractEmailForm):
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    address_ru = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    form_success_text_ru = RichTextField(blank=True, null=True)

    content_panels = RegularPage.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("phone_number"),
                FieldPanel("address_ru"),
                FieldPanel("email"),
            ],
            heading="Contact Information",
        ),
        MultiFieldPanel(
            [FieldPanel("latitude"), FieldPanel("longitude"),],
            heading="Google Maps location",
        ),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("form_success_text_ru"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    def get_context(self, request):
        context = super().get_context(request)
        context["social_links"] = SocialLink.objects.all()
        return context


@register_snippet
class SocialLink(models.Model):
    title_ru = models.CharField(max_length=128)
    icon = models.CharField(max_length=256)
    url = models.URLField()

    panels = [
        FieldPanel("title_ru"),
        FieldPanel("icon"),
        FieldPanel("url"),
    ]

    def __str__(self):
        return self.title_ru
