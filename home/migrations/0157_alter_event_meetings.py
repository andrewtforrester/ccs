# Generated by Django 4.0.8 on 2023-04-26 19:48

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0156_alter_event_meetings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='meetings',
            field=wagtail.fields.StreamField([('meeting', wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock()), ('start_time', wagtail.blocks.TimeBlock()), ('end_time', wagtail.blocks.TimeBlock(help_text='Leave blank to only display a start time.', required=False)), ('place', wagtail.blocks.CharBlock(help_text="Leave blank to use the event's default location.", required=False)), ('description', wagtail.blocks.RichTextBlock(help_text="Optional description of the meeting (e.g. the content covered in a course or reading group session, special instructions for a particular meeting, etc). Leave blank to use the event's default description.", required=False))]))], use_json_field=None),
        ),
    ]
