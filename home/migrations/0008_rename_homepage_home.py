# Generated by Django 4.0.1 on 2022-07-07 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0007_delete_samplepage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='Home',
        ),
    ]
