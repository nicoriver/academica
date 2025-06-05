from django.db import models
from datetime import datetime

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre_carrera
    
    class Meta:
        db_table = 'Carrera'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

class Usuario(models.Model):
    #id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=50, null=False)
    f_nac = models.DateTimeField( null=False)
    f_registro = models.DateTimeField(auto_now_add=True, null=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class PlanEstudio(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombre_plan = models.CharField(max_length=150)
    fecha_vigencia = models.DateField()                                                                                                                                                                                                                                                         
    
    def __str__(self):
        return self.carrera
    
    class Meta:
        db_table = 'PlanEstudio'
        verbose_name = 'Plan de Estudio'
        verbose_name_plural = 'Planes de Estudio'



