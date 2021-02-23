from rest_framework import serializers
from unit.models import Unit,Product_category

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Product_category
        fields = '__all__'

