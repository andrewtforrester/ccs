# Generated by Django 4.0.8 on 2023-01-20 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_rename_banner_3_feature_image_homepage_what_we_do_feature_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_2_feature_image',
            new_name='what_we_believe_feature_image',
        ),
    ]
