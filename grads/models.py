from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
import datetime

# Create your models here.

# GRAD STUDENTS

class GradStudents(Page):
    is_creatable = False
    subpage_types = [
        'grads.GraduateChristianScholars',
        'grads.ChristianScholarshipWorkshop'
    ]

class GraduateChristianScholars(Page):

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

class ChristianScholarshipWorkshop(Page):

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