from rest_framework import serializers
from locker.models import Cabinet,Lockers

class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'

class LockersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lockers
        fields = '__all__'
        extra_kwargs={
            "code":{"allow_blank":True},
            "name":{"allow_blank":True},
            "mode":{"allow_blank":True}       
        }