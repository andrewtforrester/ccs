# Generated by Django 4.0.8 on 2023-01-14 12:52

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_ourstaffentry_description_ourstaffentry_job_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourstaffentry',
            name='type',
            field=wagtail.fields.RichTextField(choices=[('staff', 'Staff'), ('boardOfDirectors', 'Board of Directors'), ('advisoryBoard', 'Advisory Board')], default='staff'),
            preserve_default=False,
        ),
    ]
