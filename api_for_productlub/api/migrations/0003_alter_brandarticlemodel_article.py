# Generated by Django 4.1.2 on 2022-10-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_brandarticlemodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandarticlemodel',
            name='article',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
