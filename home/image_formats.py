from django.utils.translation import ugettext_lazy as _
from wagtail.images.formats import (
    Format,
    register_image_format,
    unregister_image_format,
)

unregister_image_format("fullwidth")
unregister_image_format("left")
unregister_image_format("right")

register_image_format(
    Format("fullwidth", _("Full width"), "richtext-image full-width", "width-1200")
)
register_image_format(
    Format("left", _("Left-aligned"), "richtext-image left", "width-600")
)
register_image_format(
    Format("right", _("Right-aligned"), "richtext-image right", "width-600")
)
