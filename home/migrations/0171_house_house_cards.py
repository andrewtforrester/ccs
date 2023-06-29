# Generated by Django 4.0.8 on 2023-06-28 19:49

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0170_readinggroup_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='house_cards',
            field=wagtail.fields.StreamField([('image_card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('text_card', wagtail.blocks.StructBlock([('title_text', wagtail.blocks.CharBlock()), ('body_text', wagtail.blocks.RichTextBlock()), ('button_text', wagtail.blocks.CharBlock()), ('button_reference', wagtail.blocks.CharBlock())])), ('hours_card', wagtail.blocks.StructBlock([('title_text', wagtail.blocks.CharBlock()), ('hours_text', wagtail.blocks.StreamBlock([('house_hours_entry', wagtail.blocks.StructBlock([('title_text_entry', wagtail.blocks.CharBlock()), ('hours_text_entry', wagtail.blocks.CharBlock())]))]))]))], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]
