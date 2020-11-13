 
from rest_framework import generics

from ..models.planes_materias import PlanMateria
from ..serializers.planes_materias import (PlanMateriaListSerializer,
                                   PlanMateriaCreateSerializer,
                                   PlanMateriaRetrieveSerializer)


class PlanMateriaList(generics.ListCreateAPIView):
    queryset = PlanMateria.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlanMateriaListSerializer
        return PlanMateriaCreateSerializer


class PlanMateriaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlanMateria.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlanMateriaRetrieveSerializer
        return PlanMateriaCreateSerializer
