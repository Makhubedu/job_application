# Generated by Django 3.0.5 on 2020-05-22 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobpost',
            options={'managed': True, 'verbose_name': 'JobPost', 'verbose_name_plural': 'JobPosts'},
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='publisher',
            new_name='author',
        ),
        migrations.AlterModelTable(
            name='jobpost',
            table='job_posts',
        ),
    ]
