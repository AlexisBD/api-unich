from rest_framework import generics

# ---- Models ----
from ..models.materia import Materia

# ---- Serializer ----
from ..serializers.materia import (MateriaListSerializer,
                                    MateriaCreateSerializer)
                                    
class MateriaList(generics.ListCreateAPIView):
    queryset = Materia.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MateriaListSerializer
        return MateriaCreateSerializer


class MateriaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materia.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MateriaListSerializer
        return MateriaCreateSerializer