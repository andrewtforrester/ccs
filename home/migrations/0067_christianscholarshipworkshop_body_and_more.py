# Generated by Django 4.0.8 on 2023-02-08 21:31

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0066_continuingeducation_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='christianscholarshipworkshop',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], default='', use_json_field=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graduatechristianscholars',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]
