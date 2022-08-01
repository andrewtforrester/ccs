from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class Home(Page):
    body = RichTextField(blank=True)
    is_creatable = False
    # subpage_types = ['pages.SitePage']

    template = "home/home_page.html"

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]