# Generated by Django 4.0.8 on 2023-06-30 02:22

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0198_give'),
    ]

    operations = [
        migrations.AddField(
            model_name='give',
            name='footer_links',
            field=wagtail.fields.StreamField([('card', wagtail.blocks.StructBlock([('card_color', wagtail.blocks.ChoiceBlock(choices=[('rose', 'Rose'), ('navy', 'Navy'), ('white', 'White'), ('burgundy', 'Burgundy')])), ('text_side_content', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('button_reference', wagtail.blocks.CharBlock())]))], use_json_field=True)), ('image', wagtail.images.blocks.ImageChooserBlock())]))], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]
