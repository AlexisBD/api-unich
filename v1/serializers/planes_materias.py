 
from rest_framework import serializers

from ..models.plan import Plan
from ..models.planes_materias import PlanMateria
from ..models.carrera import Carrera
from ..models.materia import Materia
from ..models.eje import Eje


from .materia import MateriaListSerializer

class PlanMateriaListSerializer(serializers.ModelSerializer):
    """ Serializer para listar todos Planes-Materias. """
    # id_materia = serializers.ReadOnlyField(source='materia_id.id')
    nombre = serializers.ReadOnlyField(source='materia_id.nombre')
    eje = serializers.ReadOnlyField(source='eje_id.nombre')
    # materias = serializers.ReadOnlyField(source='materia.nombre')
    class Meta:
        model = PlanMateria
        fields = [
            'id', 'clave', 'nombre', 'eje', 'semestre', 'creditos',
        ]
        # Todo de materia

class PlanMateriaCreateSerializer(serializers.ModelSerializer):
    """ Serializer para crear y actualizar un Planes-Materias. """
    # materia = serializers.PrimaryKeyRelatedField(
    #     queryset=Materia.objects.all(),
    #     source='materia',
    # )
    # eje = serializers.PrimaryKeyRelatedField(
    #     queryset=Eje.objects.all(),
    #     source='eje',
    # )
    # plan = serializers.PrimaryKeyRelatedField(
    #     queryset=Plan.objects.all(),
    #     source='plan',
    # )
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


class PlanMateriaReducedSerializer(serializers.ModelSerializer):
    id_materia = serializers.ReadOnlyField(source='materia_id.id')
    nombre = serializers.ReadOnlyField(source='materia_id.nombre')
    tipo = serializers.ReadOnlyField(source='materia_id.tipo')
    class Meta:
        model  = PlanMateria
        fields = [
            'id_materia', 'nombre', 'tipo'
        ]