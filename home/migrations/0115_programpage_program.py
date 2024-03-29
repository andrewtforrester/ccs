# Generated by Django 4.0.8 on 2023-04-24 17:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0114_alter_archivepage_archived_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('feature_content', wagtail.fields.StreamField([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('button_link', wagtail.blocks.CharBlock())]))], use_json_field=True)),
                ('feature_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Program',
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
    ]
