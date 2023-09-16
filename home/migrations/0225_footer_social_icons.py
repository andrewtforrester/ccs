# Generated by Django 4.0.8 on 2023-07-12 00:59

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0224_lectureindex_display_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='social_icons',
            field=wagtail.fields.StreamField([('icon', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.CharBlock())]))], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]