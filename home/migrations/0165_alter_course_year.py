# Generated by Django 4.0.8 on 2023-05-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0164_course_year_alter_course_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
