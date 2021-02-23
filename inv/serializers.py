from rest_framework import serializers
from inv.models import Product,Stock

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stock
        fields = '__all__'