# Generated by Django 2.2.1 on 2019-06-17 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchdetails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveries',
            old_name='match_id',
            new_name='match',
        ),
    ]
