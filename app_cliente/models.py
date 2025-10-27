from django.db import models

class Sucursales(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}, {self.estado}"

    class Meta:
        db_table = 'sucursales'
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    id_sucursal = models.ForeignKey(Sucursales, on_delete=models.SET_NULL, null=True, blank=True)
    foto_cliente = models.ImageField(upload_to='clientes/', null=True, blank=True)  # <- Campo nuevo

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
