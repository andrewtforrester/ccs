# Generated by Django 4.0.8 on 2023-05-22 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0169_alter_readinggroup_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='readinggroup',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]