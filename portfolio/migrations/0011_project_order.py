# Generated by Django 2.0.5 on 2018-11-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20180606_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
    ]