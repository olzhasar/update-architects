# Generated by Django 2.0.9 on 2020-09-12 11:03

from django.db import migrations


def copy_model_fields(apps, model_name, field_mapping):
    Model = apps.get_model("home", model_name)
    for record in Model.objects.all():
        for key_to, key_from in field_mapping.items():
            setattr(record, key_to, getattr(record, key_from))
        record.save(update_fields=field_mapping.keys())


def copy_ru_to_en_fields(apps, schema_editor):
    copy_model_fields(
        apps,
        "HomePage",
        {
            "title_en": "title",
            "seo_title_en": "seo_title",
            "search_description_en": "search_description",
            "body_en": "body_ru",
        },
    )
    copy_model_fields(
        apps,
        "StandardPage",
        {
            "title_en": "title",
            "seo_title_en": "seo_title",
            "search_description_en": "search_description",
            "body_en": "body_ru",
            "subtitle_en": "subtitle_ru",
        },
    )
    copy_model_fields(
        apps,
        "ServicesPage",
        {
            "title_en": "title",
            "seo_title_en": "seo_title",
            "search_description_en": "search_description",
            "body_en": "body_ru",
            "subtitle_en": "subtitle_ru",
        },
    )
    copy_model_fields(
        apps,
        "ServicePage",
        {
            "title_en": "title",
            "seo_title_en": "seo_title",
            "search_description_en": "search_description",
            "body_en": "body_ru",
            "subtitle_en": "subtitle_ru",
            "short_description_en": "short_description_ru",
        },
    )
    copy_model_fields(
        apps,
        "AboutPage",
        {
            "title_en": "title",
            "seo_title_en": "seo_title",
            "search_description_en": "search_description",
            "body_en": "body_ru",
            "subtitle_en": "subtitle_ru",
        },
    )
    copy_model_fields(
        apps, "TeamMember", {"name_en": "name_ru", "job_title_en": "job_title_ru",},
    )
    copy_model_fields(
        apps,
        "JobPostings",
        {
            "title_en": "title",
            "seo_title_en": "seo_title",
            "search_description_en": "search_description",
            "body_en": "body_ru",
            "subtitle_en": "subtitle_ru",
        },
    )
    copy_model_fields(
        apps,
        "JobPosting",
        {"job_title_en": "job_title_ru", "description_en": "description_ru",},
    )
    copy_model_fields(
        apps,
        "Contacts",
        {
            "title_en": "title",
            "seo_title_en": "seo_title",
            "search_description_en": "search_description",
            "body_en": "body_ru",
            "subtitle_en": "subtitle_ru",
            "address_en": "address_ru",
            "form_success_text_en": "form_success_text_ru",
        },
    )
    copy_model_fields(
        apps, "SocialLink", {"title_en": "title_ru"},
    )


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0047_auto_20200912_1056"),
    ]

    operations = [migrations.RunPython(copy_ru_to_en_fields)]