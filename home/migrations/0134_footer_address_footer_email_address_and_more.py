# Generated by Django 4.0.8 on 2023-04-24 22:54

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0133_alter_footer_footer_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='address',
            field=wagtail.fields.StreamField([('address_line', wagtail.blocks.CharBlock())], default='', use_json_field=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='email_address',
            field=models.CharField(default='', max_length=511),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='site_description',
            field=wagtail.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
