from django.db import models
from datetime import datetime

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=150)
    
    def __str__(self):
        return self.names
    
    class Meta:
        db_table = 'Carrera'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

