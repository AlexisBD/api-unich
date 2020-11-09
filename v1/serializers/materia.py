from rest_framework import serializers
from ..model.materia import Materia

class MateriaListSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar datos de las Materias. """
   
    class Meta:
        model = Materia
        fields = ['id', 'nombre', 'tipo']
        
class MateriaCreateSerializer(serializers.ModelSerializer):
    """ Serializer para crear y actualizar una Materia. """
    class Meta:
        model = Materia
        fields = [
            'id', 'nombre', 'tipo', 'is_seration', 'comentarios',
        ]


