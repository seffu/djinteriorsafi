# Generated by Django 3.0.7 on 2020-06-07 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Contact',
        ),
    ]