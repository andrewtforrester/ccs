# Generated by Django 4.0.8 on 2023-06-29 12:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0188_leadershipindex_advisory_board_header_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Give',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give_description', wagtail.fields.RichTextField()),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]