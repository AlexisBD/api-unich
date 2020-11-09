from django.db import models

from .mixins import TimestampMixin

class Materia(TimestampMixin):
    nombre        = models.CharField( max_length=50)
    tipo          = models.IntegerField( null=False ) #'1-normal 2-optativa 3-taller 4-tutoria'
    is_seration   = models.BooleanField(default=True)
    comentarios   = models.TextField(blank=True, null=True) 
    
    def __str__(self):
        return self.nombre




