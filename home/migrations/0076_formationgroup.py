# Generated by Django 4.0.8 on 2023-02-28 15:12

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0075_weeklywednesdaymealindex_descriptive_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormationGroup',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('header_text', models.CharField(max_length=255)),
                ('descriptive_text', wagtail.fields.RichTextField()),
                ('feature_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
