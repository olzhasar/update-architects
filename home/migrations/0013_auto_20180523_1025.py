# Generated by Django 2.0.5 on 2018-05-23 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180523_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicepage',
            old_name='content',
            new_name='body',
        ),
    ]
