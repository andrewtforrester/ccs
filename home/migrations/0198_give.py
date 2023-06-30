# Generated by Django 4.0.8 on 2023-06-30 02:13

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0197_delete_give'),
    ]

    operations = [
        migrations.CreateModel(
            name='Give',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_hero_text', wagtail.fields.RichTextField()),
                ('donation_widget_heading', wagtail.fields.RichTextField()),
                ('donation_widget_description', wagtail.fields.RichTextField()),
                ('more_options_header', wagtail.fields.RichTextField()),
                ('giving_options_background', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
