# Generated by Django 4.1.2 on 2022-10-20 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_articlefile_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandarticlemodel',
            name='file',
        ),
    ]