 
from rest_framework import serializers

from ..models.plan import Plan
from ..models.carrera import Carrera

class PlanListSerializer(serializers.ModelSerializer):
    """ Serializer para listar todos los Planes. """
    class Meta:
        model = Plan
        fields = [
            'id', 'rvoe', 'descripcion', 'modular', 'ano', 'duracion',            
        ] 
        # Todo de materias


class PlanCreateSerializer(serializers.ModelSerializer):
    """ Serializer para crear y actualizar un Plan. """
    carrera = serializers.PrimaryKeyRelatedField(
        queryset=Carrera.objects.all(),
        source='carrera',
    )
    class Meta:
        model = Plan
        fields = [
            'id', 'rvoe', 'descripcion', 'ano', 'duracion', 'num_creditos',
            'num_materias', 'num_parciales', 'num_extras', 'max_extras','max_faltas',
            'max_dms','max_dms_promedio','modular','carrera_id'
        ] 


class PlanRetrieveSerializer(serializers.ModelSerializer):
    """ Serializer para listar un solo Plan. """
    class Meta:
        model = Plan
        fields = [
            'id', 'rvoe', 'descripcion', 'ano', 'duracion', 'num_creditos',
            'num_materias', 'num_parciales', 'num_extras', 'max_extras','max_faltas',
            'max_dms','max_dms_promedio','modular'
        ] 
