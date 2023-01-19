from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    east_campus_map = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    houseSlides = StreamField([
        ('photo', ImageChooserBlock(required=True)),
    ], use_json_field=True, blank=True, null=True)

    banner_2_feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    offerings = StreamField([
        ('offering', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.RichTextBlock()),
            ('photo', ImageChooserBlock(required=False)),
            ('button_text', blocks.CharBlock()),
            ('button_link', blocks.CharBlock()),
        ])),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('cover_image'),
        FieldPanel('banner_2_feature_image'),
        FieldPanel('east_campus_map'),
        FieldPanel('offerings'),
        FieldPanel('houseSlides'),
    ]

# ABOUT

class About(Page):
    pass

class OurStaffIndex(Page):

    subpage_types = [
        'home.OurStaffEntry'
    ]

class OurStaffEntry(Page):
    name = RichTextField(features=[])
    job_title = RichTextField(features=[])

    staff_type_choices = [
        ('staff','Staff'),
        ('boardOfDirectors','Board of Directors'),
        ('advisoryCouncil','Faculty Advisory Council'),
    ]

    type = RichTextField(features=[], choices=staff_type_choices)
    description = RichTextField()
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('job_title'),
        FieldPanel('type', widget=forms.Select),
        FieldPanel('description'),
        FieldPanel('photo'),
    ]

    subpage_types = []

class OurFaculty(Page):
    pass

# STUDENTS

class IncomingStudents(Page):
    pass

class CertificationPathway(Page):
    pass

class FellowsProgram(Page):
    pass

class ShortCoursesIndex(Page):
    pass

class ShortCoursesEntry(Page):
    name = RichTextField(features=[])
    instructor = RichTextField(features=[])
    registration_link = RichTextField(features=[])
    meeting_schedule = RichTextField(features=[])
    location = RichTextField(features=[])
    description = RichTextField()
    poster = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('instructor'),
        FieldPanel('registration_link'),
        FieldPanel('meeting_schedule'),
        FieldPanel('location'),
        FieldPanel('description'),
        FieldPanel('poster'),
    ]

    subpage_types = []


class MentorshipOpportunities(Page):
    pass

class GradStudents(Page):
    pass

# FACULTY

# FRIENDS

# OTHER

class House(Page):
    pass

class CurrentEvents(Page):
    pass

class Donate(Page):
    pass