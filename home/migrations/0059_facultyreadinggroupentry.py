# Generated by Django 4.0.8 on 2023-01-20 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0058_christianscholarshipworkshop_continuingeducation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyReadingGroupEntry',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
