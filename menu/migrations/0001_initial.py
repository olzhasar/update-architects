# Generated by Django 2.0.9 on 2020-11-22 13:38

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtailmenus.models.menuitems


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomMainMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='link to a custom URL')),
                ('url_append', models.CharField(blank=True, help_text="Use this to optionally append a #hash or querystring to the above page's URL.", max_length=255, verbose_name='append to URL')),
                ('handle', models.CharField(blank=True, help_text='Use this field to optionally specify an additional value for each menu item, which you can then reference in custom menu templates.', max_length=100, verbose_name='handle')),
                ('link_text', models.CharField(blank=True, help_text="Provide the text to use for a custom URL, or set on an internal page link to use instead of the page's title.", max_length=255, verbose_name='link text')),
                ('allow_subnav', models.BooleanField(default=True, help_text="NOTE: The sub-menu might not be displayed, even if checked. It depends on how the menu is used in this project's templates.", verbose_name='allow sub-menu for this item')),
                ('link_text_en', models.CharField(blank=True, max_length=250)),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page', verbose_name='link to an internal page')),
                ('menu', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_menu_items', to='wagtailmenus.MainMenu')),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
                'ordering': ('sort_order',),
                'abstract': False,
            },
            bases=(models.Model, wagtailmenus.models.menuitems.MenuItem),
        ),
    ]
