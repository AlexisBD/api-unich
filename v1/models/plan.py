 
from django.db import models

from .mixins import TimestampMixin
from .carrera import Carrera

class Plan(TimestampMixin):
    rvoe                = models.CharField( max_length=20 )    
    descripcion         = models.CharField(max_length=200)
    modular             = models.IntegerField()
    ano                 = models.CharField( max_length=4 )
    duracion            = models.SmallIntegerField(max_length=6) 
    num_creditos        = models.SmallIntegerField(max_length=6) 
    num_materias        = models.SmallIntegerField(max_length=6) 
    num_parciales       = models.IntegerField()
    num_extras          = models.IntegerField()
    max_extras          = models.IntegerField()   
    max_faltas          = models.IntegerField()   
    max_dms             = models.IntegerField()    
    max_dms_promedio    = models.IntegerField()      
    carrera_id          = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    max_dms             = models.IntegerField()

    def __str__(self):
        return self.descripcion