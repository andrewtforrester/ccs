# Generated by Django 4.0.8 on 2023-01-19 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_evententry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evententry',
            name='name',
        ),
    ]
