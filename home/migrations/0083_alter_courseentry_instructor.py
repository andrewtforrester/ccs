# Generated by Django 4.0.8 on 2023-03-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0082_readinggroup_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseentry',
            name='instructor',
            field=models.CharField(blank=True, max_length=127),
        ),
    ]
