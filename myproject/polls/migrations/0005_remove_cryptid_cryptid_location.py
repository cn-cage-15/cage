# Generated by Django 3.0.8 on 2020-07-23 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200723_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptid',
            name='cryptid_location',
        ),
    ]