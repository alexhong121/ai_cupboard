from rest_framework import serializers
from access.models import Locker_access,UI_access
from users.serializers import ProfilesSerializer
from locker.serializers import LockersSerializer

class Locker_accSerializers(serializers.ModelSerializer):
    Profiles_ids=ProfilesSerializer(many=True, read_only=True)
    Lockers_ids=LockersSerializer(many=True, read_only=True)

    class Meta:
        model= Locker_access
        fields="__all__"


class UI_accessSerializers(serializers.ModelSerializer):


    class Meta:
        model = UI_access
        fields = "__all__"
        


