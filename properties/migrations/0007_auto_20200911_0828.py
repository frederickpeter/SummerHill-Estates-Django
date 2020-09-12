# Generated by Django 3.1 on 2020-09-11 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20200903_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'ordering': ['name'], 'verbose_name_plural': '3. Apartments'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'ordering': ['name'], 'verbose_name_plural': '4. Facilities'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['name'], 'verbose_name': 'Property', 'verbose_name_plural': '1. Properties'},
        ),
        migrations.AlterModelOptions(
            name='property_facility',
            options={'verbose_name_plural': '5. Property Facilities'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-date'], 'verbose_name_plural': '6. Reservations'},
        ),
        migrations.AlterModelOptions(
            name='room_type',
            options={'ordering': ['capacity'], 'verbose_name': 'Room-Type', 'verbose_name_plural': '2. Room Types'},
        ),
        migrations.AlterField(
            model_name='apartment',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='properties.room_type'),
        ),
    ]
