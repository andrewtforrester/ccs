# Generated by Django 4.0.8 on 2023-02-26 20:48

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0068_constructionpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructionpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]
