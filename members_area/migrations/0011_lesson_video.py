# Generated by Django 2.2.9 on 2020-02-05 14:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members_area', '0010_auto_20200130_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='video'),
        ),
    ]