# Generated by Django 4.0.8 on 2023-07-12 01:00

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0225_footer_social_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='social_icons',
            field=wagtail.fields.StreamField([('icon', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.CharBlock())]))], blank=True, null=True, use_json_field=True),
        ),
    ]
