# Generated by Django 4.0.8 on 2023-04-20 23:04

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0110_alter_courseentry_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseentry',
            name='category',
            field=wagtail.fields.RichTextField(choices=[('Short Course', 'Short Course'), ('Duke Course', 'Duke Course')]),
        ),
    ]