# Generated by Django 2.0.5 on 2018-05-21 10:29

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((), default=''),
            preserve_default=False,
        ),
    ]
