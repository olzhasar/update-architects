# Generated by Django 2.0.9 on 2020-09-12 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20190721_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioindex',
            old_name='body',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='portfolioindex',
            old_name='subtitle',
            new_name='subtitle_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='area_size',
            new_name='area_size_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='authors',
            new_name='authors_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='description_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='location',
            new_name='location_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='status',
            new_name='status_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='subtitle',
            new_name='subtitle_ru',
        ),
        migrations.RenameField(
            model_name='projectcategory',
            old_name='name',
            new_name='name_ru',
        ),
    ]
