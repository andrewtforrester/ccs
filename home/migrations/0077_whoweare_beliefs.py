# Generated by Django 4.0.8 on 2023-02-28 15:17

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0076_formationgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='whoweare',
            name='beliefs',
            field=wagtail.fields.StreamField([('belief', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]