# Generated by Django 4.0.8 on 2023-01-19 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_evententry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evententry',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
