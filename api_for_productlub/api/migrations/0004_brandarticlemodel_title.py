# Generated by Django 4.1.2 on 2022-10-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_brandarticlemodel_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandarticlemodel',
            name='title',
            field=models.CharField(max_length=350, null=True),
        ),
    ]
