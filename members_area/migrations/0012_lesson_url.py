# Generated by Django 2.2.9 on 2020-02-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members_area', '0011_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='url',
            field=models.URLField(blank=True, max_length=350, null=True),
        ),
    ]
