# Generated by Django 4.0.8 on 2023-07-05 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0221_course_canonical_url_course_og_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectureindex',
            name='active_header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lectureindex',
            name='archive_header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
