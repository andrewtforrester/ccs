# Generated by Django 4.0.8 on 2023-04-24 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0125_globaldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='globaldata',
            name='message',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
