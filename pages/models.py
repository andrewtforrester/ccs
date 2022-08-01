from dataclasses import Field
from pydoc import classname
from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock

class About(Page):

    # settings

    subpage_types = []
    template = "about.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class Programming(Page):

    # settings

    subpage_types = []
    template = "programming.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class Fellows(Page):

    # settings

    subpage_types = []
    template = "fellows.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class Resources(Page):

    # settings

    subpage_types = []
    template = "resources.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class IncomingStudents(Page):

    # settings

    subpage_types = []
    template = "incomingstudents.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class House(Page):

    # settings

    subpage_types = []
    template = "house.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class OurPeople(Page):

    # settings

    subpage_types = ['pages.StaffMember']
    template = "ourpeople.html"
    is_creatable = False

    # fields

    CCS_staff = StreamField([
        ('staff_member', blocks.StructBlock([
            ('first_name', blocks.CharBlock()),
            ('last_name', blocks.CharBlock()),
            ('position', blocks.CharBlock()),
            ('headshot', ImageChooserBlock(required=False)),
            ('biography', blocks.RichTextBlock()),
        ]))
    ], collapsed=True)

    # CCS_house_staff = StreamField([
    #     ('student_staffer', blocks.StructBlock([
    #         ('first_name', blocks.CharBlock()),
    #         ('last_name', blocks.CharBlock()),
    #         ('headshot', ImageChooserBlock(required=False)),
    #         ('year', blocks.CharBlock()),
    #         ('major', blocks.CharBlock()),
    #     ]))
    # ], collapsed=True)

    # CCS_faculty_affiliates = StreamField([
    #     ('faculaty_affiliate', blocks.StructBlock([
    #         ('first_name', blocks.CharBlock()),
    #         ('last_name', blocks.CharBlock()),
    #         ('headshot', ImageChooserBlock(required=False)),
    #     ]))
    # ], collapsed=True, blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('CCS_staff'),
        # FieldPanel('CCS_house_staff'),
        # FieldPanel('CCS_faculty_affiliates'),
    ]

class StaffMember(Page):
    
    # settings

    subpage_types = []
    parent_page_types = ['pages.OurPeople']
    template = "people/_entry.html"
    is_creatable = True

    # fields

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('first_name',classname='full'),
        FieldPanel('last_name',classname='full'),
        FieldPanel('job_title',classname='full'),
    ]

class EventCalendar(Page):

    # settings

    subpage_types = ['pages.Event']
    template = "eventcalendar.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class Event(Page):
    
    # settings

    subpage_types = []
    parent_page_types = ['pages.EventCalendar']
    template = "events/_entry.html"
    is_creatable = True

    # fields

    event_name = models.CharField(max_length=300)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('event_name',classname='full'),
    ]

class WhoWeAre(Page):

    # settings

    subpage_types = []
    template = "whoweare.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class WhatWeDo(Page):

    # settings

    subpage_types = []
    template = "whatwedo.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class ContactUs(Page):

    # settings

    subpage_types = []
    template = "contactus.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]

class Donate(Page):

    # settings

    subpage_types = []
    template = "donate.html"
    is_creatable = False

    # fields

    body = RichTextField(blank=True)

    # panels

    content_panels = Page.content_panels + [
        FieldPanel('body',classname='full'),
    ]