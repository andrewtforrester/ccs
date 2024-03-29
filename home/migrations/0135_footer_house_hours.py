# Generated by Django 4.0.8 on 2023-04-24 22:55

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0134_footer_address_footer_email_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='house_hours',
            field=wagtail.fields.StreamField([('hour', wagtail.blocks.CharBlock())], default='', use_json_field=None),
            preserve_default=False,
        ),
    ]
