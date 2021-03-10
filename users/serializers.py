from rest_framework import serializers
from users.models import Profiles,Departments,Questions,Quest_answers
from utils.base import DataFormat,content
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings

from utils.base import DataFormat
#######################alex 2020/09/23 app 登录##############################

class DepartmentsSerializer(serializers.ModelSerializer):
    # test

    class Meta:
        model = Departments
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    # test
    class Meta:
        model = User
        fields = '__all__'



class AuthUserSeriForProfiles(serializers.ModelSerializer):						
    # test						
    class Meta:						
        model = User						
        fields = ['username','is_superuser']						


class ProfilesSerializer(serializers.ModelSerializer):
    # AuthUser_id=AuthUserSeriForProfiles(many=True, read_only=True)

    class Meta:
        model= Profiles
        fields='__all__'

    def to_representation(self, instance):
       ret = super().to_representation(instance)
       ret['AuthUser_id'] = AuthUserSeriForProfiles(instance.AuthUser_id).data
       return ret

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.alias=validated_data.get('alias', instance.alias)
        instance.Departments_id = validated_data.get('Departments_id', instance.Departments_id)
        instance.AuthUser_id = validated_data.get('AuthUser_id', instance.AuthUser_id)
        instance.save()
        return instance

class QuestionsSerializer(serializers.ModelSerializer):
    # test
    class Meta:
        model = Questions
        fields = '__all__'



class Quest_answersSerializer(serializers.ModelSerializer):
     # test
    class Meta:
        model = Quest_answers
        fields = '__all__'
        


class MyTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        # data = {'access': str(refresh.access_token)}
        data = content(types='success',data={'access': str(refresh.access_token)})

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()

            data['refresh'] = str(refresh)

        return data

