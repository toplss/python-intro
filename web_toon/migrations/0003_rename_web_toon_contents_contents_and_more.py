# Generated by Django 4.2.6 on 2023-10-17 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_toon', '0002_web_toon_web_toon_contents_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='web_toon_contents',
            new_name='Contents',
        ),
        migrations.RenameModel(
            old_name='web_toon',
            new_name='Post',
        ),
    ]
