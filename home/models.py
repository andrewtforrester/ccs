from django.db import models
from django import forms
from wagtailseo.models import SeoMixin

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList, PageChooserPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
import datetime
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class Header(BaseSetting):
    navigation = StreamField([
        ('category', blocks.StructBlock([
            ('category_name', blocks.CharBlock()),
            ('category_links', blocks.StreamBlock([
                ('internal_link', blocks.StructBlock([
                    ('link_text', blocks.CharBlock()),
                    ('link_reference', blocks.PageChooserBlock()),
                ])),
                ('external_link', blocks.StructBlock([
                    ('link_text', blocks.CharBlock()),
                    ('link_reference', blocks.CharBlock()),
                ])),
            ]))
        ])),
        ('internal_button', blocks.StructBlock([
            ('button_text', blocks.CharBlock()),
            ('button_link', blocks.PageChooserBlock()),
        ])),
        ('external_button', blocks.StructBlock([
            ('button_text', blocks.CharBlock()),
            ('button_link', blocks.CharBlock()),
        ])),
    ], use_json_field=True)

@register_setting
class Footer(BaseSetting):

    site_description = RichTextField()

    address = StreamField([
        ('address_line', blocks.CharBlock())
    ])

    house_hours = StreamField([
        ('hour', blocks.CharBlock())
    ])

    email_address = models.CharField(max_length=511)
    mailto_link = models.CharField(max_length=511)

    ccs_house_header_text = models.CharField(max_length=511)
    ccs_house_header_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )


    
    footer_links = StreamField([
        ('category', blocks.StructBlock([
            ('category_name', blocks.CharBlock()),
            ('category_links', blocks.StreamBlock([
                ('internal_link', blocks.StructBlock([
                    ('link_text', blocks.CharBlock()),
                    ('link_reference', blocks.PageChooserBlock()),
                ])),
                ('external_link', blocks.StructBlock([
                    ('link_text', blocks.CharBlock()),
                    ('link_reference', blocks.CharBlock()),
                ])),
            ]))
        ])),
    ], use_json_field=True)

    general_information = [
        FieldPanel('site_description'),
        MultiFieldPanel([
            FieldPanel('ccs_house_header_text'),
            PageChooserPanel('ccs_house_header_link'),
        ], heading="CCS House Heading"),
        FieldPanel('address'),
        FieldPanel('house_hours'),
        MultiFieldPanel([
            FieldPanel('email_address'),
            FieldPanel('mailto_link'),
        ], heading="Email Address"),
    ]

    footer_navigation = [
        FieldPanel('footer_links'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(general_information, heading='General Information'),
        ObjectList(footer_navigation, heading='Footer Navigation'),
    ])

    panels = [
        FieldPanel('footer_links')
    ]

class CustomPage(SeoMixin, Page):
    is_creatable = True

    color_options = [
        ('rose','Rose'),
        ('navy','Navy'),
        ('white','White'),
        ('burgundy','Burgundy'),
    ]

    overlay_options = [
        ('none','None'),
        ('navy','Navy'),
    ]

    page_content = StreamField([
        ('article_section', blocks.StructBlock([
            ('background_color', blocks.ChoiceBlock(choices=color_options)),
            ('article_content', blocks.StreamBlock([
                ('heading', blocks.CharBlock()),
                ('paragraph', blocks.RichTextBlock()),
                ('image', ImageChooserBlock()),
                ('button', blocks.StructBlock([
                    ('button_text', blocks.CharBlock()),
                    ('button_reference', blocks.CharBlock()),
                ])),
            ])),
        ])),


        ('text_and_image_full_section', blocks.StructBlock([
            ('background_color', blocks.ChoiceBlock(choices=color_options)),
            ('text_side_content', blocks.StreamBlock([
                ('heading', blocks.CharBlock()),
                ('paragraph', blocks.RichTextBlock()),
                ('button', blocks.StructBlock([
                    ('button_text', blocks.CharBlock()),
                    ('button_reference', blocks.CharBlock()),
                ])),
            ], use_json_field=True)),
            ('featured_image', ImageChooserBlock()),
            ('image_overlay', blocks.ChoiceBlock(choices=overlay_options)),
        ])),


        ('card_collection_section', blocks.StructBlock([
            ('background_color', blocks.ChoiceBlock(choices=color_options)),
            ('title', blocks.CharBlock(required=False)),
            ('cards', blocks.StreamBlock([
                ('image_card', blocks.StructBlock([
                    ('image', ImageChooserBlock()),
                ])),
                ('text_card', blocks.StructBlock([
                    ('card_color', blocks.ChoiceBlock(choices=color_options)),
                    ('content', blocks.StreamBlock([
                        ('heading', blocks.CharBlock()),
                        ('paragraph', blocks.RichTextBlock()),
                        ('button', blocks.StructBlock([
                            ('button_text', blocks.CharBlock()),
                            ('button_reference', blocks.CharBlock()),
                        ])),
                    ], use_json_field=True)),
                ])),
                ('text_and_image_card', blocks.StructBlock([
                    ('card_color', blocks.ChoiceBlock(choices=color_options)),
                    ('text_side_content', blocks.StreamBlock([
                        ('heading', blocks.CharBlock()),
                        ('paragraph', blocks.RichTextBlock()),
                        ('button', blocks.StructBlock([
                            ('button_text', blocks.CharBlock()),
                            ('button_reference', blocks.CharBlock()),
                        ])),
                    ], use_json_field=True)),
                    ('image', ImageChooserBlock()),
                ])),
            ], collapsed=True, use_json_field=True)),
        ])),

        ('contact_section', blocks.StructBlock([
            ('background_color', blocks.ChoiceBlock(choices=color_options)),
            ('headshot', ImageChooserBlock()),
            ('body_text', blocks.CharBlock()),
            ('button', blocks.StructBlock([
                ('button_text', blocks.CharBlock()),
                ('button_reference', blocks.CharBlock()),
            ])),
        ]))


    ], collapsed=True, use_json_field=True)



    content_panels = Page.content_panels + [
        StreamFieldPanel('page_content'),
    ]

    

# HOMEPAGE

class HomePage(SeoMixin, Page):
    is_creatable = False
    dark_background = True
    # Helper Methods

    def events(self):
        return CurrentEvents.events(CurrentEvents)[:3]

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
        ObjectList(SeoMixin.seo_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])

    subpage_types = ['home.CustomPage']


# ABOUT

class WhoWeAre(Page):
    dark_background = True

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
    dark_background = True

    leadership_description = RichTextField(blank=True, null=True)

    staff_members_displayed = StreamField([
        ('staff_member', blocks.PageChooserBlock(
            page_type=[
                "home.LeadershipEntry",
            ]
        )),
    ], use_json_field=True)

    def staff(self):
        return LeadershipEntry.objects.filter(type='staff').specific()
    
    def board(self):
        return LeadershipEntry.objects.filter(type='boardOfDirectors').order_by('last_name').specific()
    
    def advisors(self):
        return LeadershipEntry.objects.filter(type='advisoryCouncil').order_by('last_name').specific()

    content_panels = Page.content_panels + [
        FieldPanel('leadership_description'), 
        FieldPanel('staff_members_displayed'), 
    ]

    subpage_types = [
        'home.LeadershipEntry'
    ]

class LeadershipEntry(Page):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)

    def full_name(self):
        return self.first_name.strip() + " " + self.last_name.strip()

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
        FieldPanel('first_name'), 
        FieldPanel('last_name'), 
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


# COMMUNITY

class House(SeoMixin, Page):

    dark_background = True

    header_text = models.CharField(max_length=255)
    descriptive_text = RichTextField()
    feature_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    house_cards = StreamField([
        ('image_card', blocks.StructBlock([
            ('image', ImageChooserBlock()),
        ])),
        ('text_card', blocks.StructBlock([
            ('title_text', blocks.CharBlock()),
            ('body_text', blocks.RichTextBlock()),
            ('button_text', blocks.CharBlock()),
            ('button_reference', blocks.CharBlock()),
        ])),
        ('hours_card', blocks.StructBlock([
            ('title_text', blocks.CharBlock()),
            ('hours_text', blocks.StreamBlock([
                ('house_hours_entry', blocks.StructBlock([
                    ('title_text_entry', blocks.CharBlock()),
                    ('hours_text_entry', blocks.CharBlock()),
                ])),
            ])),
        ])),
    ], use_json_field=True)

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

    # programming_title_text = models.CharField(max_length=255)

    # house_programming = StreamField([
    #     ('program', blocks.StructBlock([
    #         ('title', blocks.CharBlock()),
    #         ('extra_text', blocks.RichTextBlock(required=False)),
    #         ('button_text', blocks.CharBlock()),
    #         ('button_reference', blocks.CharBlock()),
    #         ('feature_image', ImageChooserBlock()),
    #     ])),
    # ], use_json_field=True)

    # content_panels = Page.content_panels + [
        # FieldPanel('programming_title_text'),
        # FieldPanel('house_programming'),
    # ]

    head_panel = [
        FieldPanel('header_text'),
        FieldPanel('descriptive_text'),
        FieldPanel('feature_image'),
    ]

    card_panel = [
        FieldPanel('house_cards'),
    ]

    map_panel = [
        FieldPanel('map_title_text'),
        FieldPanel('map_description_text'),
        FieldPanel('map_button_text'),
        FieldPanel('map_button_link'),
        FieldPanel('east_campus_map'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(head_panel, heading='Header'),
        ObjectList(card_panel, heading='Cards'),
        ObjectList(map_panel, heading='Map'),
        ObjectList(SeoMixin.seo_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])

    is_creatable = False
    subpage_types = []

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

class CurrentEvents(Page):
    is_creatable = False
    def events(self):

        y = datetime.date.today().year
        m = datetime.date.today().month
        d = datetime.date.today().day

        result = []

        for event in Event.objects.live():
            for meeting in event.meetings:
                if meeting.value['date'] >= datetime.date(year=y,month=m,day=d):
                    result = result + [({
                        "title": event.title,
                        "description": event.description,
                        "associated_page": event.associated_page.url if event.associated_page else event.url,
                        "date": meeting.value['date'],
                        "start_time": meeting.value['start_time'],
                        "end_time": meeting.value['end_time'],
                    })]

        return sorted(result, key = lambda d: d['date'])

    subpage_types = ['home.Event']

class Event(SeoMixin, Page):

    description = RichTextField(null=True, blank=True)
    registration_link = models.CharField(max_length=1023, blank=True)
    location = models.CharField(max_length=1023, blank=True)
    leader = models.CharField(max_length=1023, blank=True)

    meetings = StreamField([
        ('meeting', blocks.StructBlock([
            ('date', blocks.DateBlock()),
            ('start_time', blocks.TimeBlock()),
            ('end_time', blocks.TimeBlock(required=False, help_text='Leave blank to only display a start time.')),
            ('place', blocks.CharBlock(required=False, help_text='Leave blank to use the event\'s default location.')),
            ('description', blocks.RichTextBlock(required=False, help_text='Optional description of the meeting (e.g. the content covered in a course or reading group session, special instructions for a particular meeting, etc). Leave blank to use the event\'s default description.')),
        ]))
    ])
    
    associated_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Leave blank to associate this event with an automatically generated page.'
    )

    poster = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    general = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('location'),
        FieldPanel('registration_link'),
        FieldPanel('poster'),
        FieldPanel('associated_page'),
    ]

    mtgs = [
        FieldPanel('meetings')
    ]

    edit_handler = TabbedInterface([
        ObjectList(general, 'General Information'),
        ObjectList(mtgs, 'Meetings'),
        ObjectList(SeoMixin.seo_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('registration_link'),
        FieldPanel('location'),
        FieldPanel('poster'),
        FieldPanel('meetings'),
    ]

    def abridged_description(self):
        if len(self.description) > 350:
            return self.description[:350] + "..."
        else:
            return self.description
            
        
    subpage_types = []


# ACADEMICS



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

    active_header_text = models.CharField(max_length=255)
    archive_header_text = models.CharField(max_length=255)

    def active_items(self):
        return Course.objects.live().filter(type='active').specific()
    
    def archived_items(self):
        result = []
        temp = []
        i = 1
        if not len(Course.objects.live().filter(type='archived')) == 0:
            for course in Course.objects.live().filter(type='archived').order_by('-year','-semester','title').specific():
                temp = temp + [course]
                if len(temp) == 5:
                    result = result + [(temp,i)]
                    temp = []
                    i = i + 1

            if not temp == []:
                result = result + [(temp,i)]
        else:
            return []
        return result

    content_panels = Page.content_panels + [
        FieldPanel('header_text'),
        FieldPanel('descriptive_text'),
        FieldPanel('active_header_text'),
        FieldPanel('archive_header_text'),
    ]

    is_creatable = False
    subpage_types = ['home.Course']

class Course(Page):

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

    categories = [
        ('Short Course', 'Short Course'),
        ('Duke Course', 'Duke Course'),
    ]

    category = RichTextField(features=[], choices=categories)

    status = [
        ('future','Future'),
        ('active','Active'),
        ('archived','Archived'),
    ]

    type = RichTextField(features=[], choices=status)

    semester_options = [
        ('1_spring','Spring'),
        ('2_summer','Summer'),
        ('3_fall','Fall'),
    ]

    semester = RichTextField(features=[], choices=semester_options)
    year = models.IntegerField()

    def semester_and_year(self):
        return self.get_semester_display() + " " + str(self.year)

    content_panels = Page.content_panels + [
        FieldPanel('semester',widget=forms.Select),
        FieldPanel('year'),
        FieldPanel('instructor'),
        FieldPanel('registration_link'),
        FieldPanel('location'),
        FieldPanel('meeting_pattern'),
        FieldPanel('description'),
        FieldPanel('poster'),
        FieldPanel('category',widget=forms.Select),
        FieldPanel('type',widget=forms.Select),
    ]

    def abridged_description(self):
        if len(self.description) > 350:
            return self.description[:350] + "..."
        else:
            return self.description

    subpage_types = []


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

    active_header_text = models.CharField(max_length=255)
    archive_header_text = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('header_text'),
        FieldPanel('descriptive_text'),
        FieldPanel('feature_image'),
        FieldPanel('active_header_text'),
        FieldPanel('archive_header_text'),
    ]

    def active_items(self):
        return ReadingGroup.objects.live().filter(type='active').specific()
    
    def archived_items(self):
        result = []
        temp = []
        i = 1

        if not len(ReadingGroup.objects.live().filter(type='archived')) == 0:
            for course in ReadingGroup.objects.live().filter(type='archived').specific():
                temp = temp + [course]
                if len(temp) == 5:
                    result = result + [(temp,i)]
                    temp = []
                    i = i + 1

            if not temp == []:
                result = result + [(temp,i)]
            return result
        else:
            return []
    
    is_creatable = False
    subpage_types = ['home.ReadingGroup']

class ReadingGroup(Page):

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
        ('future','Future'),
        ('active','Active'),
        ('archived','Archived'),
    ]

    type = RichTextField(features=[], choices=status)

    semester_options = [
        ('1_spring','Spring'),
        ('2_summer','Summer'),
        ('3_fall','Fall'),
    ]

    def semester_and_year(self):
        return self.get_semester_display() + " " + str(self.year)

    year = models.IntegerField()


    semester = RichTextField(features=[], choices=semester_options)

    content_panels = Page.content_panels + [
        FieldPanel('semester',widget=forms.Select),
        FieldPanel('year'),
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

    subpage_types = []



class LectureIndex(Page):
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

    def active_items(self):
        return Lecture.objects.live().filter(type='active').specific()
    
    def archived_items(self):
        result = []
        temp = []
        i = 1

        for course in Lecture.objects.live().filter(type='archived').specific().order_by('date'):
            temp = temp + [course]
            if len(temp) == 5:
                result = result + [(temp,i)]
                temp = []
                i = i + 1

        if not temp == []:
            result = result + [(temp,i)]
        return result
    
    is_creatable = False
    subpage_types = ['home.Lecture']

class Lecture(Page):
    description = RichTextField(blank=True)
    speaker = models.CharField(max_length=1023, blank=True)
    registration_link = models.CharField(max_length=1023, blank=True)
    archival_link = models.CharField(max_length=1023, blank=True)
    location = models.CharField(max_length=1023, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    status = [
        ('future','Future'),
        ('active','Active'),
        ('archived','Archived'),
    ]

    type = RichTextField(features=[], choices=status)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('speaker'),
        FieldPanel('registration_link'),
        FieldPanel('archival_link'),
        FieldPanel('location'),
        FieldPanel('date'),
        FieldPanel('time'),
        FieldPanel('featured_image'),
        FieldPanel('type', widget=forms.Select),
    ]

    def abridged_description(self):
        if len(self.description) > 350:
            return self.description[:350] + "..."
        else:
            return self.description

    subpage_types = []


class ConferenceIndex(Page):
    is_creatable = False

    subpage_types = [
        'home.Conference'
    ]

class Conference(Page):
    pass




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
            ('semester', blocks.CharBlock()),
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
        FieldPanel('eligable_courses'),
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



# SUPPORT

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

class FellowsProgramIndex(Page):
    pass

class SummerProgramsIndex(Page):
    pass
