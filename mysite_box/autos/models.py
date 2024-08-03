from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

# tipos de usuarios que se pueden registrar
USER_TYPE_CHOICES = [

	('Standard', 'Standard'),
    ('Pro', 'Pro'),

]

# Todas las marcas de autos disponibles. 
BRAND_CHOICES = [
    ('Fiat','Fiat'),
    ('Renault','Renault'),
    ('Toyota','Toyota'),
]

# todos los servicios que se le pueden hacer a un auto
SERVICE_TYPE_CHOICES = [

('Filtro de aire', 'Filtro de aire'),
('Filtro de aceite', 'Filtro de aceite'),
('Cambio aceite', 'Cambio aceite'),
('Cambio pastillas de freno', 'Cambio pastillas de freno'),
('Filtro de combustible', 'Filtro de combustible'),
('Cambio de lubricación de transmisión', 'Cambio de lubricación de transmisión'),
('Cambio de amortiguadores', 'Cambio de amortiguadores'),
('Cambio de cubiertas', 'Cambio de cubiertas'),
('Cambio de batería', 'Cambio de batería'),
('Carga Combustible', 'Carga Combustible'),
('Chapista', 'Chapista'),
('Tren delantero', 'Tren delantero'),
('Electricidad', 'Electricidad'),
('Carga Nafta', 'Carga Nafta'),
('Pinchadura', 'Pinchadura'),
('Me hizo un ruido', 'Me hizo un ruido'),
('Cualquier otra cosa', 'Cualquier otra cosa'),

]


# Registro de usuarios de la plataforma
class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.EmailField(max_length=254, blank=False, verbose_name='Correo Electrónico')
    phone = models.CharField(max_length=15, blank=True, default='090 000 000', verbose_name='Número de Celular')
    city = models.CharField(max_length=50, blank=False, verbose_name="Ciudad")
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Standard', verbose_name='Tipo de Usuario')
    created_at = models.DateField(auto_now_add=True, verbose_name='Fecha Registro')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @admin.display(description='Nombre')
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# Registro de talleres y mecánicos
class Mechanic(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    garage = models.CharField(max_length=50, verbose_name='Nombre del Taller')
    address = models.CharField(max_length=100, verbose_name='Dirección')
    city = models.CharField(max_length=100, blank=False, verbose_name="Ciudad")
    phone = models.CharField(max_length=15, blank=True, default='090 000 000', verbose_name='Número de Celular')
    email = models.EmailField(max_length=254, blank=False, verbose_name='Codeo Electrónico (Opcional)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')

    def __str__(self):
        return self.garage
    
    @admin.display(description='Nombre')
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# Aqui los usuarios pueden registrar sus vehiculos.
# IMPORTANTE: Los usuarios YA DEBEN estár registrados en la plataforma para poder registrar
class Vehicle(models.Model):

    def current_year():
        return datetime.date.today().year
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Titular')
    plate = models.CharField(max_length=10, verbose_name='Patente')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name='Marca')
    moddel = models.CharField(max_length=50, verbose_name='Modelo')
    year = models.IntegerField(default=current_year, verbose_name='Año de Fabricación')
    color = models.CharField(max_length=50, verbose_name='Color')
    car_mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Fecha Creación')
    
    def __str__(self):
        return self.plate


# listamos los servicios que puede recibir el vehiculo
class Service(models.Model):
    
    def current_year():
        return datetime.date.today().year
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Patente')
    date = models.DateField(default=timezone.now, verbose_name='Fecha Servicio')
    kilometers = models.IntegerField(default=0, verbose_name='Kilometraje')
    service_type = models.CharField(max_length=500, choices=SERVICE_TYPE_CHOICES, verbose_name='Tipo de Servicio')
    coments = models.TextField(verbose_name='Comentarios', blank=True, help_text="Indique cualquier cosa que desee comentar")
    cost = models.IntegerField(verbose_name='Costo del Servicio')
    created_at = models.DateField(auto_now_add=True, verbose_name='Fecha Servicio')

    def __str__(self):
        return self.service_type