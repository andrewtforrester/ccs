# Generated by Django 4.0.8 on 2023-02-28 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0070_coursesindex_descriptive_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseentry',
            name='type',
        ),
    ]
