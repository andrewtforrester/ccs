# Generated by Django 4.0.8 on 2023-01-14 18:58

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_homepage_east_campus_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='offerings',
            field=wagtail.fields.StreamField([('offering', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.RichTextBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_text', wagtail.blocks.CharBlock()), ('button_link', wagtail.blocks.CharBlock())]))], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]
