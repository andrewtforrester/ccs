from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
import datetime


class HomePage(Page):

    # Helper Methods

    def events(self):

        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month)
        d = str(datetime.date.today().day)

        events = EventInstance.objects.live().public().filter(date__range=[y+"-"+m+"-"+d, "9999-01-01"]).order_by('date')[:3]
        return events

    # BANNER

    banner_title_text = models.CharField(max_length=255)
    banner_button_text = models.CharField(max_length=255)
    banner_button_link = models.CharField(max_length=255)
    
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    

    # WHAT WE BELIEVE

    we_believe_title_text = models.CharField(max_length=255)
    we_believe_description_text = RichTextField()
    we_believe_button_text = models.CharField(max_length=255)
    we_believe_button_link = models.CharField(max_length=255)

    we_believe_feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # WHAT WE DO

    what_we_do_header = models.CharField(max_length=255)

    what_we_do_feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    what_we_do = StreamField([
        ('item', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.RichTextBlock()),
            ('button_text', blocks.CharBlock()),
            ('button_link', blocks.CharBlock()),
        ])),
    ], use_json_field=True)


    # WHAT WE OFFER

    what_we_offer_heading = models.CharField(max_length=255)

    offerings = StreamField([
        ('offering', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.RichTextBlock()),
            ('photo', ImageChooserBlock(required=False)),
            ('button_text', blocks.CharBlock()),
            ('button_link', blocks.CharBlock()),
        ])),
    ], use_json_field=True)

    # SLIDESHOW

    slides_header_text = models.CharField(max_length=255)

    houseSlides = StreamField([
        ('photo', ImageChooserBlock(required=True)),
    ], use_json_field=True, blank=True, null=True)
   
    # MAP
    
    east_campus_map = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    map_title_text = models.CharField(max_length=255)
    map_description_text = RichTextField()
    map_button_text = models.CharField(max_length=255)
    map_button_link = models.CharField(max_length=255)


    bnr = [
        FieldPanel('banner_title_text'),
        FieldPanel('banner_button_text'),
        FieldPanel('banner_button_link'),
        FieldPanel('cover_image'),
    ]

    wwb = [
        FieldPanel('we_believe_feature_image'),
        FieldPanel('we_believe_title_text'),
        FieldPanel('we_believe_description_text'),
        FieldPanel('we_believe_button_text'),
        FieldPanel('we_believe_button_link'),
    ]

    wwd = [
        FieldPanel('what_we_do_header'),
        FieldPanel('what_we_do_feature_image'),
        FieldPanel('what_we_do'),
    ]

    off = [
        FieldPanel('what_we_offer_heading'),
        FieldPanel('offerings'),
    ]

    slideshow = [
        FieldPanel('slides_header_text'),
        FieldPanel('houseSlides'),
    ]

    map_tab = [
        FieldPanel('map_title_text'),
        FieldPanel('map_description_text'),
        FieldPanel('map_button_text'),
        FieldPanel('map_button_link'),
        FieldPanel('east_campus_map'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(bnr, heading='Homepage Banner'),
        ObjectList(wwb, heading='What We Believe'),
        ObjectList(wwd, heading='What We Do'),
        ObjectList(off, heading='What We Offer'),
        ObjectList(slideshow, heading='Slideshow'),
        ObjectList(map_tab, heading='East Campus Map'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])

    

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
    instructor = RichTextField()
    registration_link = models.CharField(max_length=1023)
    location = models.CharField(max_length=1023)
    meeting_pattern = models.CharField(max_length=1023)
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
        FieldPanel('meeting_pattern'),
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
