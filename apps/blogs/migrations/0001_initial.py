# Generated by Django 3.0.7 on 2020-06-07 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('blog_image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('blog_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]