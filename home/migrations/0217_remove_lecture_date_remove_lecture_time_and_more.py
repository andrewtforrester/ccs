# Generated by Django 4.0.8 on 2023-07-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0216_alter_course_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='date',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='time',
        ),
        migrations.AddField(
            model_name='lecture',
            name='date_and_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
