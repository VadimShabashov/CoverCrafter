# Generated by Django 4.2.6 on 2023-10-14 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_file_actual_path'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='VideoFile',
        ),
    ]
