# Generated by Django 4.2.6 on 2023-10-17 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_toon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='web_toon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('coverimg', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='web_toon_contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('wt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_toon.web_toon')),
            ],
        ),
        migrations.RemoveField(
            model_name='webtooncontent',
            name='wt_id',
        ),
        migrations.DeleteModel(
            name='WebToon',
        ),
        migrations.DeleteModel(
            name='WebToonContent',
        ),
    ]
