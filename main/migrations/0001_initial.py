# Generated by Django 4.1 on 2022-08-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_path', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=60)),
                ('eof', models.BooleanField()),
            ],
        ),
    ]
