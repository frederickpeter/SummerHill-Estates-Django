# Generated by Django 3.1 on 2020-08-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20200830_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='decription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(max_length=80, unique=True),
        ),
    ]
