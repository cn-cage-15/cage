# Generated by Django 3.0.8 on 2020-07-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20200723_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptid',
            name='first_mentioned',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
