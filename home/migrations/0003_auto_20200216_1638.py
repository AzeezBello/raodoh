# Generated by Django 2.2.9 on 2020-02-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200131_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='avatar',
        ),
    ]