# Generated by Django 3.0.8 on 2020-07-23 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200723_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptid',
            old_name='cryptit_location',
            new_name='cryptid_location',
        ),
    ]
