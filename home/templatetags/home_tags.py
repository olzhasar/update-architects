from django import template

from home.models import SocialLink

register = template.Library()


@register.inclusion_tag("home/tags/social_links.html", takes_context=True)
def social_links(context):
    return {
        "social_links": SocialLink.objects.all(),
        "request": context["request"],
    }
