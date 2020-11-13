from rest_framework import serializers

from ..models.eje import Eje

class EjeListSerializer(serializers.ModelSerializer):
    """ Serializer para mostrar datos de Ejes. """


    class Meta:
        model = Eje
        fields = ['id', 'clave', 'nombre']

class EjeCreateSerializer(serializers.ModelSerializer):
    """ Serializer para crear y actualizar un Eje. """
    class Meta:
        model = Eje
        fields = [
            'id', 'clave', 'nombre',
        ]


