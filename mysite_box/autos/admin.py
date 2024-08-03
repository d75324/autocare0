from django.contrib import admin
from .models import User, Service, Vehicle, Mechanic


# muestra los registros en el modelo User
class UserBE(admin.ModelAdmin):
	list_display = (
        'created_at',
        'full_name',
        'email',
        'phone',
        'city',
        'user_type',
    )
	search_fields = (
		'created_at',
		'full_name',
		'city',
    )

admin.site.register(User, UserBE)


# muestra el listado de los mecánicos
class MechanicBE(admin.ModelAdmin):
	list_display = (
		'created_at',
        'full_name',
        'garage',
        'address',
        'city',
        'phone',
        'email',		
    )
	search_fields = (
		'created_at',
		'full_name',
		'garage',
		'city',
    )
	
admin.site.register(Mechanic, MechanicBE)


# muestra los vehiculos registrados
class VehicleBE(admin.ModelAdmin):
	list_display = (
        'created_at',
        'owner',
        'plate',
        'brand',
        'moddel',
        'year',
        'color',
        'car_mechanic',
    )
	search_fields = (
		'created_at',
		'plate',
		'car_mechanic',
    )
	
admin.site.register(Vehicle, VehicleBE)


# muestra los servicios realizados
class ServiceBE(admin.ModelAdmin):
	list_display = (
        'vehicle',
        'date',
        'kilometers',
        'service_type',
        'coments',
        'cost',
    )
	search_fields = (
		'vehicle',
		'date',
		'service_type',
    )

admin.site.register(Service, ServiceBE)
