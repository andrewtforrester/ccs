# Generated by Django 4.0.8 on 2023-05-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0157_alter_event_meetings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadershipentry',
            name='name',
            field=models.TextField(max_length=255),
        ),
    ]
