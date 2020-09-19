# Generated by Django 3.1 on 2020-09-19 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name must be a maximum of 50 characters', max_length=50, unique=True)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Booked', 'Booked')], default='Available', max_length=20)),
            ],
            options={
                'verbose_name_plural': '3. Apartments',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name must be a maximum of 100 characters', max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': '4. Facilities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name must be a maximum of 150 characters', max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(help_text='Name must be a maximum of 4000 characters', max_length=4000)),
                ('image1', models.ImageField(max_length=254, upload_to='images/')),
                ('image2', models.ImageField(blank=True, max_length=254, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, max_length=254, null=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, max_length=254, null=True, upload_to='images/')),
                ('image5', models.ImageField(blank=True, max_length=254, null=True, upload_to='images/')),
                ('brochure', models.FileField(blank=True, max_length=254, null=True, upload_to='documents/')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': '1. Properties',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Room_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField()),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image1', models.ImageField(blank=True, max_length=254, null=True, upload_to='images/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_types', to='properties.property')),
            ],
            options={
                'verbose_name': 'Room-Type',
                'verbose_name_plural': '2. Room Types',
                'ordering': ['capacity'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=30)),
                ('duration_type', models.CharField(choices=[('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month'), ('Year', 'Year')], max_length=30)),
                ('duration', models.PositiveSmallIntegerField(help_text='Example. 2 Years')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('first_payment', models.CharField(choices=[('Paid', 'Paid'), ('No Payment', 'No Payment')], default='No Payment', max_length=15)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='properties.apartment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '6. Reservations',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Property_Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='properties.facility')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='properties.property')),
            ],
            options={
                'verbose_name_plural': '5. Property Facilities',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='facilities',
            field=models.ManyToManyField(through='properties.Property_Facility', to='properties.Facility'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='properties.reservation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_time'],
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='properties.room_type'),
        ),
        migrations.AddConstraint(
            model_name='room_type',
            constraint=models.UniqueConstraint(fields=('capacity', 'property'), name='unique_room_types'),
        ),
    ]
