# Generated by Django 4.0.8 on 2023-04-24 17:55

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0116_programpage_archived_programs_header_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeProgram',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('semester', models.CharField(blank=True, max_length=1023)),
                ('instructor', models.CharField(blank=True, max_length=1023)),
                ('registration_link', models.CharField(blank=True, max_length=1023)),
                ('location', models.CharField(blank=True, max_length=1023)),
                ('meeting_pattern', models.CharField(blank=True, max_length=1023)),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('type', wagtail.fields.RichTextField(choices=[('active', 'Active'), ('archived', 'Archived')])),
                ('poster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RecurringProgram',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('semester', models.CharField(blank=True, max_length=1023)),
                ('instructor', models.CharField(blank=True, max_length=1023)),
                ('registration_link', models.CharField(blank=True, max_length=1023)),
                ('location', models.CharField(blank=True, max_length=1023)),
                ('meeting_pattern', models.CharField(blank=True, max_length=1023)),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('type', wagtail.fields.RichTextField(choices=[('active', 'Active'), ('archived', 'Archived')])),
                ('poster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RecurringProgramInstance',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='Program',
        ),
    ]
