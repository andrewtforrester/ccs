# Generated by Django 4.0.8 on 2023-02-28 06:26

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0074_whoweare_mission_header_whoweare_mission_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklywednesdaymealindex',
            name='descriptive_text',
            field=wagtail.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weeklywednesdaymealindex',
            name='feature_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='weeklywednesdaymealindex',
            name='header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
