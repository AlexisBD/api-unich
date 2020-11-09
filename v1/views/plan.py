 
from rest_framework import generics

from ..models.plan import Plan
from ..serializers.plan import (PlanListSerializer,
                                   PlanCreateSerializer,
                                   PlanRetrieveSerializer)


class PlanList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlanListSerializer
        return PlanCreateSerializer


class PlanDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlanRetrieveSerializer
        return PlanCreateSerializer
