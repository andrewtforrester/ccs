# Generated by Django 4.0.8 on 2023-04-05 13:49

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0092_leadershipindex_leadership_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyaffiliatesindex',
            name='faculty_description',
            field=wagtail.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
