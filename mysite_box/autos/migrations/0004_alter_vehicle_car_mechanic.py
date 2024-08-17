# Generated by Django 5.0.7 on 2024-08-17 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0003_alter_user_created_at_alter_vehicle_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='car_mechanic',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='autos.mechanic', verbose_name='Mecánico Asignado'),
        ),
    ]
