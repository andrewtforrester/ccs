# Generated by Django 4.0.8 on 2023-04-11 13:31

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0093_facultyaffiliatesindex_faculty_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='house_programming',
            field=wagtail.fields.StreamField([('program', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('meeting_pattern', wagtail.blocks.CharBlock()), ('feature_image', wagtail.images.blocks.ImageChooserBlock())]))], default='', use_json_field=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='programming_title_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
