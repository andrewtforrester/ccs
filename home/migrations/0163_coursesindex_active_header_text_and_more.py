# Generated by Django 4.0.8 on 2023-05-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0162_rename_name_leadershipentry_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesindex',
            name='active_header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursesindex',
            name='archive_header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='readinggroupsindex',
            name='active_header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='readinggroupsindex',
            name='archive_header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
