# Generated by Django 4.0.8 on 2023-01-20 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0049_courseentry_meeting_pattern'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OurStaffIndex',
            new_name='LeadershipIndex',
        ),
    ]
