# Generated by Django 4.2.6 on 2023-10-17 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_toon', '0004_alter_contents_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contents',
            old_name='wt_id',
            new_name='wt',
        ),
    ]
