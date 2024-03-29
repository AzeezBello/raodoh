# Generated by Django 2.2.9 on 2020-01-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members_area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(related_name='lesson', to='members_area.Category'),
        ),
    ]
