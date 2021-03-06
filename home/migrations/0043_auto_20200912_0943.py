# Generated by Django 2.0.9 on 2020-09-12 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_servicepage_wiki_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpage',
            old_name='body',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='aboutpage',
            old_name='subtitle',
            new_name='subtitle_ru',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='address',
            new_name='address_ru',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='body',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='form_success_text',
            new_name='form_success_text_ru',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='subtitle',
            new_name='subtitle_ru',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='body',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='jobposting',
            old_name='description',
            new_name='description_ru',
        ),
        migrations.RenameField(
            model_name='jobposting',
            old_name='job_title',
            new_name='job_title_ru',
        ),
        migrations.RenameField(
            model_name='jobpostings',
            old_name='body',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='jobpostings',
            old_name='subtitle',
            new_name='subtitle_ru',
        ),
        migrations.RenameField(
            model_name='servicepage',
            old_name='body',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='servicepage',
            old_name='short_description',
            new_name='short_description_ru',
        ),
        migrations.RenameField(
            model_name='servicepage',
            old_name='subtitle',
            new_name='subtitle_ru',
        ),
        migrations.RenameField(
            model_name='servicespage',
            old_name='body',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='servicespage',
            old_name='subtitle',
            new_name='subtitle_ru',
        ),
        migrations.RenameField(
            model_name='sociallink',
            old_name='title',
            new_name='title_ru',
        ),
        migrations.RenameField(
            model_name='standardpage',
            old_name='body',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='standardpage',
            old_name='subtitle',
            new_name='subtitle_ru',
        ),
        migrations.RenameField(
            model_name='teammember',
            old_name='job_title',
            new_name='job_title_ru',
        ),
        migrations.RenameField(
            model_name='teammember',
            old_name='name',
            new_name='name_ru',
        ),
    ]
