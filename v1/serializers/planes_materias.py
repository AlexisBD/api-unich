 
from rest_framework import serializers

from ..models.planes_materias import PlanMateria
from ..models.plan import Plan
from ..models.carrera import Carrera
from ..models.eje import Eje
from ..models.materia import Materia

class PlanMateriaListSerializer(serializers.ModelSerializer):
    """ Serializer para listar todos Planes-Materias. """
    class Meta:
        model = PlanMateria
        fields = [
            'id', 'clave', 'eje_id', 'semestre', 'creditos',            
        ] 
        # Todo de materias


class PlanMateriaCreateSerializer(serializers.ModelSerializer):
    """ Serializer para crear y actualizar un Planes-Materias. """
    materia = serializers.PrimaryKeyRelatedField(
        queryset=Materia.objects.all(),
        source='materia',
    )
    eje = serializers.PrimaryKeyRelatedField(
        queryset=Eje.objects.all(),
        source='eje',
    )
    plan = serializers.PrimaryKeyRelatedField(
        queryset=Plan.objects.all(),
        source='plan',
    )
    class Meta:
        model = PlanMateria
        fields = [
            'id', 'clave', 'semestre', 'horas_docente', 'horas_independientes', 'horas_campo',
            'creditos', 'materia_id', 'eje_id', 'plan_id','parent_at'
        ] 


class PlanMateriaRetrieveSerializer(serializers.ModelSerializer):
    """ Serializer para listar un solo Plan. """
    class Meta:
        model = PlanMateria
        fields = [
            'id', 'clave', 'semestre', 'horas_docente', 'horas_independientes', 'horas_campo',
            'creditos', 'eje_id'
        ]
