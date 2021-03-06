from django.utils.translation import pgettext_lazy

from ...core.utils.text import strip_html_and_truncate
from ..widgets import CharsLeftWidget

MIN_TITLE_LENGTH = 25
MIN_DESCRIPTION_LENGTH = 120
SEO_HELP_TEXTS = {
    "seo_description": pgettext_lazy(
        "Form field help text",
        ("If empty, the preview shows what will be autogenerated."),
    ),
    "seo_title": pgettext_lazy(
        "Form field help text",
        ("If empty, the preview shows what will be autogenerated."),
    ),
}
SEO_LABELS = {
    "seo_description": pgettext_lazy(
        ("Field name, Meta Description is page summary " "used by Search Engines"),
        "Meta Description",
    ),
    "seo_title": pgettext_lazy(
        ("Field name, " "Title that will be used to describe page in Search Engines"),
        "SEO Title",
    ),
}
SEO_WIDGETS = {"seo_description": CharsLeftWidget, "seo_title": CharsLeftWidget}


def prepare_seo_description(seo_description, html_description, max_length):
    # if there is no SEO friendly description set,
    # generate it from the HTML description
    if not seo_description:
        # get the non-safe description (has non escaped HTML tags in it)
        # generate a SEO friendly from HTML description
        seo_description = strip_html_and_truncate(html_description, max_length)
    return seo_description
