from django.db import models

from .mixins import TimestampMixin


class Eje(TimestampMixin):
    clave        = models.CharField( max_length=2 )
    nombre       = models.CharField( max_length=30 )
        
    def __str__(self):
        return self.nombre