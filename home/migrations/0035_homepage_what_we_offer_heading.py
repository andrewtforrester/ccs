# Generated by Django 4.0.8 on 2023-01-20 16:08

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_homepage_what_we_do'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='what_we_offer_heading',
            field=wagtail.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
