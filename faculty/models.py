from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
import datetime

# Create your models here.

class Faculty(Page):
    is_creatable = False

    subpage_types = [
        'faculty.TriangleRoundtable',
        'faculty.FacultyReadingGroups',
        'faculty.ScholarshipWorkshop',
    ]


class TriangleRoundtable(Page):

    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    is_creatable = False
    subpage_types = []

class FacultyReadingGroups(Page):

    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    
    is_creatable = False
    subpage_types = [
        'faculty.FacultyReadingGroupEntry'
    ]

class FacultyReadingGroupEntry(Page):
    subpage_types = []

class ScholarshipWorkshop(Page):

    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    is_creatable = False
    subpage_types = []

