from django.db import models

nacional_extranjero= [
    (1, 'Nacional'),
    (2, 'Extranjero')
]
tipo_Documento=[
    (1, 'DUI'),
    (2, 'Pasaporte')
]
estado_actual=[
    (1, 'Fuera del Paìs'),
    (2, 'En el Pais')
]
tipo_alarma = [
    (1, 'Alarma 1'),
    (2, 'Alarma 2')
]
class persona(models.Model):
    idPersona = models.AutoField(primary_key=True)
    pasaporte = models.CharField(max_length=9, unique=True, default="", null=True,blank=True)
    dui = models.CharField(max_length=10, unique=True, default="", null=True,blank=True)
    nombre = models.CharField(max_length= 50, default="")
    apellido = models.CharField(max_length=50, default="")
    tipoDocumento = models.IntegerField(
        blank=True,
        choices=tipo_Documento
    ) 
    nacionalidad = models.IntegerField(
        blank=True,
        choices=nacional_extranjero
    ) 
    estado = models.IntegerField(
        blank=True,
        choices=estado_actual
    )
    

class Entrada(models.Model):
    persona = models.ForeignKey('persona', on_delete=models.CASCADE, null=True)
    fechaIngreso = models.DateField()
    TiempoPermanencia = models.CharField(max_length=10, default="",blank=True)
    paisOrigen = models.CharField(max_length=10, default="")

class Salida(models.Model):
    persona = models.ForeignKey('persona', on_delete=models.CASCADE, null=True)
    fechaSalida = models.DateField()
    TiempoPermanencia = models.CharField(max_length=10, default="",blank=True)
    paisDestino = models.CharField(max_length=10, default="")

class Alarma(models.Model):
    persona = models.ForeignKey('persona', on_delete=models.CASCADE, null=True)
    tipoAlerta = models.IntegerField(
        blank=True,
        choices=tipo_alarma
    )
    descripcion = models.TextField(max_length=200,blank = True, default="")