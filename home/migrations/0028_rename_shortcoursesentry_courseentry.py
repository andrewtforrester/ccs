# Generated by Django 4.0.8 on 2023-01-20 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0027_shortcoursesentry_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShortCoursesEntry',
            new_name='CourseEntry',
        ),
    ]
