# Generated by Django 4.1.2 on 2022-10-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_brandarticlemodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlefile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
