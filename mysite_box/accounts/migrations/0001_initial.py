# Generated by Django 5.0.7 on 2024-08-21 01:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('image', models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ciudad')),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código Postal')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Barrio')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('garage', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre del Taller')),
                ('professional_license', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.URLField(blank=True, null=True, verbose_name='Sitio Web')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['-created_at'],
            },
        ),
    ]
