 
from django.db import models

from .mixins import TimestampMixin
from .plan import Plan
from .eje import Eje
from .materia import Materia

class PlanMateria(TimestampMixin):
    clave               = models.CharField( max_length=20 )
    semestre            = models.IntegerField( null=False ) 
    horas_docente       = models.IntegerField( null=False ) 
    horas_independientes= models.IntegerField( null=False ) 
    horas_campo         = models.IntegerField( null=False ) 
    creditos            = models.IntegerField( null=False ) 
    parent_at           = models.IntegerField( null=False )  
    materia_id          = models.ForeignKey(Materia, on_delete=models.CASCADE)
    eje_id              = models.ForeignKey(Eje, on_delete=models.CASCADE)       
    plan_id             = models.ForeignKey(Plan, on_delete=models.CASCADE)       