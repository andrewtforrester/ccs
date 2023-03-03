# Generated by Django 4.0.8 on 2023-02-08 21:21

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_remove_facultyaffiliatesentry_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyreadinggroups',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], default='', use_json_field=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scholarshipworkshop',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], default='', use_json_field=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triangleroundtable',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]