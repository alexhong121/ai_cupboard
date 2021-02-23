from rest_framework import serializers
from systems.models import Configuration,Information

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'