from django.contrib import admin
from .models import Cliente, Sucursales

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    raw_id_fields = ('id_sucursal',)

@admin.register(Sucursales)
class SucursalesAdmin(admin.ModelAdmin):
    pass
