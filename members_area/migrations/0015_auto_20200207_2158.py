# Generated by Django 2.2.9 on 2020-02-07 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members_area', '0014_auto_20200206_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='url',
            new_name='video_url',
        ),
    ]