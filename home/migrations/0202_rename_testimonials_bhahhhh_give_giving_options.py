# Generated by Django 4.0.8 on 2023-06-30 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0201_give_testimonials_bhahhhh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='give',
            old_name='testimonials_bhahhhh',
            new_name='giving_options',
        ),
    ]
