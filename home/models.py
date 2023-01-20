from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
import datetime


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

    banner_3_feature_image = models.ForeignKey(
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

    def events(self):

        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month)
        d = str(datetime.date.today().day)

        events = EventInstance.objects.live().public().filter(date__range=[y+"-"+m+"-"+d, "9999-01-01"]).order_by('date')[:3]
        return events

    content_panels = Page.content_panels + [
        FieldPanel('cover_image'),
        FieldPanel('banner_2_feature_image'),
        FieldPanel('banner_3_feature_image'),
        FieldPanel('east_campus_map'),
        FieldPanel('offerings'),
        FieldPanel('houseSlides'),
    ]

# ABOUT

class WhoWeAre(Page):
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

class CoursesIndex(Page):
    subpage_types = ['home.CourseEntry']

class CourseEntry(Page):

    course_type_choices = [
        ('readingGroup','Reading Group'),
        ('shortCourse','Short Course'),
    ]

    type = RichTextField(features=[], choices=course_type_choices, blank=True, null=True)
    instructor = RichTextField(features=[])
    registration_link = RichTextField(features=[])
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
        FieldPanel('type', widget=forms.Select),
        FieldPanel('instructor'),
        FieldPanel('registration_link'),
        FieldPanel('location'),
        FieldPanel('description'),
        FieldPanel('poster'),
    ]

    def abridged_description(self):
        if len(self.description) > 300:
            return self.description[:300] + "..."
        else:
            return self.description

    subpage_types = ['home.EventInstance']


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

    def events(self):

        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month)
        d = str(datetime.date.today().day)

        events = EventInstance.objects.live().public().filter(date__range=[y+"-"+m+"-"+d, "9999-01-01"]).order_by('date')
        return events

    subpage_types = ['home.Event']

class Event(Page):

    description = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]
    
    subpage_types = ['home.EventInstance']

    def abridged_description(self):
        if len(self.description) > 300:
            return self.description + "..."
        else:
            return self.description

class EventInstance(Page):

    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('time'),
    ]

    subpage_types = []

class Give(Page):
    pass
