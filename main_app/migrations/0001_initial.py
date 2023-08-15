# Generated by Django 4.2.4 on 2023-08-15 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airbase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airbase_name', models.CharField(max_length=400)),
                ('location', models.CharField(max_length=400)),
                ('country', models.CharField(max_length=400)),
                ('airbase_type', models.CharField(max_length=400)),
                ('area_km2', models.DecimalField(decimal_places=3, max_digits=9)),
                ('runway_length_km', models.CharField(max_length=400)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=400)),
                ('manufacturer', models.CharField(max_length=400)),
                ('role', models.CharField(max_length=400)),
                ('crew', models.CharField(max_length=400)),
                ('service_years', models.CharField(max_length=400)),
                ('length_m', models.DecimalField(decimal_places=3, max_digits=9)),
                ('width_m', models.DecimalField(decimal_places=3, max_digits=9)),
                ('height_m', models.DecimalField(decimal_places=3, max_digits=9)),
                ('powerplant', models.CharField(max_length=400)),
                ('max_speed_kmh', models.DecimalField(decimal_places=3, max_digits=9)),
                ('cruise_speed_kmh', models.DecimalField(decimal_places=3, max_digits=9)),
                ('range_km', models.DecimalField(decimal_places=3, max_digits=9)),
                ('max_altitude_m', models.DecimalField(decimal_places=3, max_digits=9)),
                ('capacity', models.TextField(max_length=2000)),
                ('airbases', models.ManyToManyField(to='main_app.airbase')),
            ],
        ),
        migrations.CreateModel(
            name='Maintainance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Maintainace Date')),
                ('maintain', models.CharField(choices=[('R', 'Repairs'), ('F', 'Re-fuel'), ('A', 'Re-arm'), ('S', 'Re-supply')], default='R', max_length=1)),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.aircraft')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
