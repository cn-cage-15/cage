# Generated by Django 3.0.8 on 2020-07-23 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_cryptid_cryptid_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location_text',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='votes',
        ),
    ]
