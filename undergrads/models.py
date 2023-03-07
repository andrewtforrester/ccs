from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# UNDERGRADS

class Undergrads(Page):
    is_creatable = False

    subpage_types = [
        'undergrads.FormationGroup',
        'undergrads.IncomingStudents',
        'undergrads.CertificationPathway',
        'undergrads.FellowsProgram',
    ]


class FormationGroup(Page):
    header_text = models.CharField(max_length=255)
    descriptive_text = RichTextField()
    feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('header_text'),
        FieldPanel('descriptive_text'),
        FieldPanel('feature_image'),
    ]

    is_creatable = False


class IncomingStudents(Page):
    is_creatable = False
    subpage_types = []

class CertificationPathway(Page):
    is_creatable = False
    subpage_types = []

class FellowsProgram(Page):
    is_creatable = False
    subpage_types = []