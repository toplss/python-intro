# Generated by Django 4.2.6 on 2023-10-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_toon', '0003_rename_web_toon_contents_contents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
