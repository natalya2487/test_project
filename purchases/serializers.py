from rest_framework import serializers

from . import models


class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaterialType
        fields = ('url', 'id', 'name')


class StdProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StandardProduct
        fields = ('url', 'id', 'name', 'code')


class AssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Assembly
        fields = ('url', 'id', 'name', 'expendable_set', 'materialexpendables')


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Component
        fields = ('url', 'id', 'name')


class StdProdExpendableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StandardProductExpendable
        fields = ('url', 'id', 'assembly', 'std_prod', 'name', 'price', 'quantity', 'summ', 'stock_availability',
                  'estimated_delivery', 'notes',)


class MaterialExpendableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaterialExpendable
        fields = ('url', 'id', 'assembly', 'component', 'material', 'name', 'price', 'quantity', 'summ', 'stock_availability',
                  'estimated_delivery', 'notes', )


class ExpendableSerializer(serializers.ModelSerializer):
    type = serializers.ReadOnlyField(default=None)

    class Meta:
        model = models.Expendable
        fields = ('url', 'id', 'assembly', 'component', 'name', 'price', 'quantity', 'summ', 'stock_availability',
                  'estimated_delivery', 'notes', 'type', 'materialexpendable', 'standardproductexpendable')


class SubcontractActionSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(source='expendable.price')
    quantity = serializers.FloatField(source='expendable.quantity', default=1)
    summ = serializers.FloatField()
    estimated_delivery = serializers.IntegerField()
    notes = serializers.CharField()

    class Meta:
        model = models.SubcontractAction
        fields = ('url', 'id', 'contract', 'operation', 'price', 'quantity', 'summ',
                  # 'stock_availability',
                  'estimated_delivery', 'notes',)

    def create(self, validated_data):
        # price =
        
        instance = super().create(validated_data)
        return instance


class PurchaseSerializer(serializers.ModelSerializer):
    expendable_object = ExpendableSerializer(source='expendable', read_only=True)

    class Meta:
        model = models.Purchase
        fields = ('url', 'id', 'expendable', 'expendable_object', 'price', 'quantity', 'summ', )


