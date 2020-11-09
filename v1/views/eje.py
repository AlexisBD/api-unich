from rest_framework import generics

# ---- Models ----
from ..models.eje import Eje

# ---- Serializer ----
from ..serializers.eje import (EjeListSerializer,
                                    EjeCreateSerializer)
                                    
class EjeList(generics.ListCreateAPIView):
    queryset = Eje.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EjeListSerializer
        return EjeCreateSerializer


class EjeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eje.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EjeListSerializer
        return EjeCreateSerializer