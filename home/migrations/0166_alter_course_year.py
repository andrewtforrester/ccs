# Generated by Django 4.0.8 on 2023-05-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0165_alter_course_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(),
        ),
    ]