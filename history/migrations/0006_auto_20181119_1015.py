# Generated by Django 2.1.3 on 2018-11-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0005_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FilePathField(allow_folders=True, path='/work/django_projects/test_project/media', recursive=True),
        ),
    ]
