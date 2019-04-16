# Generated by Django 2.1.3 on 2018-11-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_auto_20181115_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]