# Generated by Django 4.0.8 on 2023-06-30 02:24

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0199_give_footer_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='give',
            name='footer_links',
        ),
        migrations.AddField(
            model_name='give',
            name='testimonials',
            field=wagtail.fields.StreamField([('card', wagtail.blocks.StructBlock([('card_color', wagtail.blocks.ChoiceBlock(choices=[('rose', 'Rose'), ('navy', 'Navy'), ('white', 'White'), ('burgundy', 'Burgundy')])), ('text_side_content', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('button_reference', wagtail.blocks.CharBlock())]))], use_json_field=True))]))], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]
