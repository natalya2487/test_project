from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from . import serializers


class MaterialTypeViewSet(viewsets.ModelViewSet):
    queryset = models.MaterialType.objects.all()
    serializer_class = serializers.MaterialTypeSerializer


class StdProdViewSet(viewsets.ModelViewSet):
    queryset = models.StandardProduct.objects.all()
    serializer_class = serializers.StdProductSerializer


class AssemblyViewSet(viewsets.ModelViewSet):
    queryset = models.Assembly.objects.all()
    serializer_class = serializers.AssemblySerializer


class ComponentViewSet(viewsets.ModelViewSet):
    queryset = models.Component.objects.all()
    serializer_class = serializers.ComponentSerializer


class StdProdExpendableViewSet(viewsets.ModelViewSet):
    queryset = models.StandardProductExpendable.objects.all()
    serializer_class = serializers.StdProdExpendableSerializer


class MaterialExpendableViewSet(viewsets.ModelViewSet):
    queryset = models.MaterialExpendable.objects.all()
    serializer_class = serializers.MaterialExpendableSerializer


class ExpendableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Expendable.objects.all()
    serializer_class = serializers.ExpendableSerializer


class SubcontractActionViewSet(viewsets.ModelViewSet):
    queryset = models.SubcontractAction.objects.all()
    serializer_class = serializers.SubcontractActionSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer

