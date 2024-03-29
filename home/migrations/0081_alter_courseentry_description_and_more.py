# Generated by Django 4.0.8 on 2023-03-06 14:31

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0080_remove_coursesindex_type_courseentry_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseentry',
            name='description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='courseentry',
            name='instructor',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='courseentry',
            name='location',
            field=models.CharField(blank=True, max_length=1023),
        ),
        migrations.AlterField(
            model_name='courseentry',
            name='meeting_pattern',
            field=models.CharField(blank=True, max_length=1023),
        ),
        migrations.AlterField(
            model_name='courseentry',
            name='registration_link',
            field=models.CharField(blank=True, max_length=1023),
        ),
    ]
