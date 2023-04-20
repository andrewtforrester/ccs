from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
import datetime

# HOMEPAGE

class HomePage(Page):
    is_creatable = False
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
    map_description_text = RichTextField(blank=True, null=True)
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

    mission_header = models.CharField(max_length=255)
    mission_text = RichTextField()
    mission_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    values_header = models.CharField(max_length=255)
    values_text = RichTextField()
    values_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    beliefs = StreamField([
        ('belief', blocks.StructBlock([
            ('text', blocks.RichTextBlock()),
        ])),
    ], use_json_field=True)



    content_panels = Page.content_panels + [
        FieldPanel('mission_header'),
        FieldPanel('mission_text'),
        FieldPanel('mission_image'),

        FieldPanel('values_header'),
        FieldPanel('values_text'),
        FieldPanel('values_image'),
        FieldPanel('beliefs'),
    ]


    is_creatable = False
    subpage_types = []
    
class LeadershipIndex(Page):
    is_creatable = False

    leadership_description = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('leadership_description'), 
    ]

    subpage_types = [
        'home.LeadershipEntry'
    ]

class LeadershipEntry(Page):
    name = RichTextField(features=[])
    job_title = RichTextField(features=[], blank=True, null=True)

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

class FacultyAffiliatesIndex(Page):
    is_creatable = False

    faculty_description = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('faculty_description'), 
    ]

    subpage_types = [
        'home.FacultyAffiliatesEntry'
    ]

class FacultyAffiliatesEntry(Page):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    website = models.CharField(max_length=1023)
    department = models.CharField(max_length=255)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('website'),
        FieldPanel('department'),
        FieldPanel('photo'),
    ]



    subpage_types = []

class House(Page):

    header_text = models.CharField(max_length=255)
    descriptive_text = RichTextField()
    feature_image = models.ForeignKey(
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

    map_title_text = models.CharField(max_length=255)
    map_description_text = RichTextField()
    map_button_text = models.CharField(max_length=255)
    map_button_link = models.CharField(max_length=255)

    programming_title_text = models.CharField(max_length=255)

    house_programming = StreamField([
        ('program', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('extra_text', blocks.RichTextBlock(required=False)),
            ('button_text', blocks.CharBlock()),
            ('button_reference', blocks.CharBlock()),
            ('feature_image', ImageChooserBlock()),
        ])),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('header_text'),
        FieldPanel('descriptive_text'),
        FieldPanel('feature_image'),
        FieldPanel('map_title_text'),
        FieldPanel('map_description_text'),
        FieldPanel('map_button_text'),
        FieldPanel('map_button_link'),
        FieldPanel('east_campus_map'),
        FieldPanel('programming_title_text'),
        FieldPanel('house_programming'),
    ]

    is_creatable = False
    subpage_types = []



# EVENTS HEADER

class CurrentEvents(Page):
    is_creatable = False
    def events(self):

        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month)
        d = str(datetime.date.today().day)

        events = EventInstance.objects.live().public().filter(date__range=[y+"-"+m+"-"+d, "9999-01-01"]).order_by('date')
        return events

    subpage_types = ['home.Event']

class CoursesIndex(Page):

    header_text = models.CharField(max_length=255)
    descriptive_text = RichTextField()
    feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def active_courses(self):
        return CourseEntry.objects.live().filter(type='active').specific()
    
    def archived_courses(self):
        result = []
        temp = []
        i = 1

        for course in CourseEntry.objects.live().filter(type='archived').specific():
            temp = temp + [course]
            if len(temp) == 5:
                result = result + [(temp,i)]
                temp = []
                i = i + 1

        if not temp == []:
            result = result + [(temp,i)]

        return result

    content_panels = Page.content_panels + [
        FieldPanel('header_text'),
        FieldPanel('descriptive_text'),
        FieldPanel('feature_image'),
    ]

    is_creatable = False
    subpage_types = ['home.CourseEntry']

class CourseEntry(Page):

    semester = models.CharField(max_length=127)
    instructor = models.CharField(max_length=127, blank=True)
    registration_link = models.CharField(max_length=1023, blank=True)
    location = models.CharField(max_length=1023, blank=True)
    meeting_pattern = models.CharField(max_length=1023, blank=True)
    description = RichTextField(blank=True)
    poster = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    status = [
        ('active','Active'),
        ('archived','Archived'),
    ]

    type = RichTextField(features=[], choices=status)

    content_panels = Page.content_panels + [
        FieldPanel('semester'),
        FieldPanel('instructor'),
        FieldPanel('registration_link'),
        FieldPanel('location'),
        FieldPanel('meeting_pattern'),
        FieldPanel('description'),
        FieldPanel('poster'),
        FieldPanel('type',widget=forms.Select),
    ]

    def abridged_description(self):
        if len(self.description) > 350:
            return self.description[:350] + "..."
        else:
            return self.description

    subpage_types = ['home.EventInstance']

class ReadingGroupsIndex(Page):

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

    def active_reading_groups(self):
        return ReadingGroup.objects.live().filter(type='active').specific()
    
    def archived_reading_groups(self):
        result = []
        temp = []
        i = 1

        for course in ReadingGroup.objects.live().filter(type='archived').specific():
            temp = temp + [course]
            if len(temp) == 5:
                result = result + [(temp,i)]
                temp = []
                i = i + 1

        if not temp == []:
            result = result + [(temp,i)]
        return result
    
    is_creatable = False
    subpage_types = ['home.ReadingGroup']

class ReadingGroup(Page):

    semester = models.CharField(max_length=1023, blank=True)
    instructor = models.CharField(max_length=1023, blank=True)
    registration_link = models.CharField(max_length=1023, blank=True)
    location = models.CharField(max_length=1023, blank=True)
    meeting_pattern = models.CharField(max_length=1023, blank=True)
    description = RichTextField(blank=True)
    poster = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    status = [
        ('active','Active'),
        ('archived','Archived'),
    ]

    type = RichTextField(features=[], choices=status)

    content_panels = Page.content_panels + [
        FieldPanel('semester'),
        FieldPanel('instructor'),
        FieldPanel('registration_link'),
        FieldPanel('location'),
        FieldPanel('meeting_pattern'),
        FieldPanel('description'),
        FieldPanel('poster'),
        FieldPanel('type', widget=forms.Select),
    ]

    def abridged_description(self):
        if len(self.description) > 350:
            return self.description[:350] + "..."
        else:
            return self.description

    subpage_types = ['home.EventInstance']

class WeeklyWednesdayMealIndex(Page):

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
    subpage_types = []

class LectureIndex(Page):
    is_creatable = False
    subpage_types = [
        'home.Lecture'
    ]

class Lecture(Page):
    subpage_types = []

class ConferenceIndex(Page):
    is_creatable = False

    subpage_types = [
        'home.Conference'
    ]

class Conference(Page):
    pass


# FACULTY



# FRIENDS

class ContinuingEducation(Page):

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

class LendAHand(Page):

    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_tab = [
        FieldPanel('title'),
        FieldPanel('body'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_tab, heading='Content'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])

    is_creatable = False
    subpage_types = []


# HELPERS

class Event(Page):

    description = RichTextField(null=True, blank=True)
    registration_link = models.CharField(max_length=1023, blank=True)
    location = models.CharField(max_length=1023, blank=True)
    poster = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('registration_link'),
        FieldPanel('location'),
        FieldPanel('poster'),
    ]
    
    subpage_types = ['home.EventInstance']

    def abridged_description(self):
        if len(self.description) > 350:
            return self.description[:350] + "..."
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

class ConstructionPage(Page):


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

class CertificatePathwayPage(Page):

    # GENERAL

    page_description = RichTextField()
    contact_headshot = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    contact_description = RichTextField()
    contact_button_text = models.TextField(max_length=255)
    contact_button_link = models.TextField(max_length=255)
    

    # COURSE BLOCK

    course_block_header_1 = models.TextField(max_length=255)
    course_block_header_2 = models.TextField(max_length=255)
    course_block_description = RichTextField()

    eligable_courses = StreamField([
        ('content_block', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.RichTextBlock()),
            ('button_text', blocks.CharBlock(blank=True, required=False)),
            ('button_link', blocks.CharBlock(blank=True, required=False)),
        ])),
    ], use_json_field=True)

    course_block_button_text = models.TextField(max_length=255)
    course_block_button_link = models.TextField(max_length=255)

    # PROJECT BLOCK

    project_block_header_1 = models.TextField(max_length=255)
    project_block_header_2 = models.TextField(max_length=255)
    project_block_description = RichTextField()

    eligable_projects = StreamField([
        ('content_block', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.RichTextBlock()),
            ('button_text', blocks.CharBlock(blank=True, required=False)),
            ('button_link', blocks.CharBlock(blank=True, required=False)),
        ])),
    ], use_json_field=True)

    project_block_button_text = models.TextField(max_length=255)
    project_block_button_link = models.TextField(max_length=255)

    general_panel = [
        FieldPanel('title'),
        FieldPanel('page_description'),
        FieldPanel('contact_headshot'),
        FieldPanel('contact_description'),
        FieldPanel('contact_button_text'),
        FieldPanel('contact_button_link'),
    ]

    course_block_panel = [
        FieldPanel('course_block_header_1'),
        FieldPanel('course_block_header_2'),
        FieldPanel('course_block_description'),
        # FieldPanel('eligable_courses'),
        FieldPanel('course_block_button_text'),
        FieldPanel('course_block_button_link'),
    ]

    project_block_panel = [
        FieldPanel('project_block_header_1'),
        FieldPanel('project_block_header_2'),
        FieldPanel('project_block_description'),
        FieldPanel('eligable_projects'),
        FieldPanel('project_block_button_text'),
        FieldPanel('project_block_button_link'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(general_panel, heading='General'),
        ObjectList(course_block_panel, heading='Courses Requirement'),
        ObjectList(project_block_panel, heading='Projects and Experiences Requirement'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])

    subpage_types = []

    def active_courses(self):
        return CourseEntry.objects.live().filter(type='active').specific()

class FellowsProgramIndex(Page):
    pass

class SummerProgramsIndex(Page):
    pass