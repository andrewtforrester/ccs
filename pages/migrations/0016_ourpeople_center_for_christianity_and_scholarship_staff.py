# Generated by Django 4.0.1 on 2022-07-19 07:58

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourpeople',
            name='center_for_christianity_and_scholarship_staff',
            field=wagtail.fields.StreamField([('staff_member', wagtail.blocks.StructBlock([('first_name', wagtail.blocks.CharBlock()), ('last_name', wagtail.blocks.CharBlock()), ('headshot', wagtail.images.blocks.ImageChooserBlock(required=False)), ('biography', wagtail.blocks.RichTextBlock())]))], default='', use_json_field=None),
            preserve_default=False,
        ),
    ]
