# Generated by Django 2.2.9 on 2020-02-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members_area', '0015_auto_20200207_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['create_time']},
        ),
    ]
