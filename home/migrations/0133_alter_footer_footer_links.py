# Generated by Django 4.0.8 on 2023-04-24 22:43

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0132_alter_footer_footer_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='footer_links',
            field=wagtail.fields.StreamField([('category', wagtail.blocks.StructBlock([('category_name', wagtail.blocks.CharBlock()), ('category_links', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock()), ('link_reference', wagtail.blocks.PageChooserBlock())])), ('external_link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock()), ('link_reference', wagtail.blocks.CharBlock())]))]))]))], use_json_field=True),
        ),
    ]
