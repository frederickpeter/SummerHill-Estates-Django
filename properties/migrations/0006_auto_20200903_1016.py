# Generated by Django 3.1 on 2020-09-03 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20200901_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facility',
            options={'ordering': ['name'], 'verbose_name_plural': 'facilities'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['name'], 'verbose_name_plural': 'properties'},
        ),
        migrations.AlterModelOptions(
            name='property_facility',
            options={'verbose_name_plural': 'property_facilities'},
        ),
        migrations.AddField(
            model_name='reservation',
            name='duration',
            field=models.PositiveSmallIntegerField(default=1, help_text='Example. 2 Years'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='duration_type',
            field=models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('Year', 'Year')], default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
    ]
