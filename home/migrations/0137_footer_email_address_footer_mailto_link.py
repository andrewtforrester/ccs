# Generated by Django 4.0.8 on 2023-04-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0136_remove_footer_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='email_address',
            field=models.CharField(default='', max_length=511),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='mailto_link',
            field=models.CharField(default='', max_length=511),
            preserve_default=False,
        ),
    ]
