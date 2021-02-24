from django.shortcuts import render
from django.http import Http404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status

from access.models import Locker_access,UI_access
from access.serializers import Locker_accSerializers,UI_accessSerializers
from locker.models import Lockers
from django.contrib.auth.models import User

from utils.base import filter_profiles_object,content

# Create your views here.
def newLocker_access(users_id):
    locker=Lockers.objects.all()
    print(locker)

class Locker_acclist(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        locker_access=Locker_access.objects.all()
        newLocker_access(3)
        serializers=Locker_accSerializers(locker_access,many=True)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        data=JSONParser().parse(request)

        locker_access=Locker_access(active=data['params']['active'],create_uid=User.objects.get(pk=data['create_uid']))
        locker_access.save()
        locker_access.Users_ids.set(data['params']['Users_ids'])
        locker_access.Lockers_ids.set(data['params']['Lockers_ids'])

        serializers=Locker_accSerializers(locker_access)

        return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        # return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class Locker_accDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Locker_access.objects.get(pk=pk)
        except Locker_access.DoesNotExist:
            raise Http404

    # def get(self, request, pk, format=None):
    #     locker_access = self.get_object(pk)
    #     serializer = Locker_accSerializers(locker_access)
    #     return Response(serializer.data)

    def put(self, request, pk, format=None):
        data=JSONParser().parse(request)
        locker_access = self.get_object(pk)
        users_ids=data['params'].pop('Users_ids')
        lockers_ids=data['params'].pop('Lockers_ids')
        data['params'].update({"write_uid":data['write_uid']})
        locker_access.Users_ids.set(users_ids)
        locker_access.Lockers_ids.set(lockers_ids)
        serializer = Locker_accSerializers(locker_access, data=data['params'])
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     locker_access = self.get_object(pk)
    #     locker_access.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class Per_UIAccDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,pk,format=None):
        profiles=filter_profiles_object(pk).first()
        
        if profiles:
            ui_access=UI_access.objects.filter(Profiles_id=profiles.id)
            serializers=UI_accessSerializers(ui_access,many=True)

            return Response(content(types='success',data=serializers.data),status=status.HTTP_200_OK)
        else:
            # content={
            # 'type': "error",  # 相应的状态 'success' | "error"
            # 'data': None, # 主要的数据 [ ] | { }
            # 'message':"Profiles of Data is not found"     # 错误信息
            # }

            return Response(content(types='error',message='Profiles of Data is not found'),status=status.HTTP_400_BAD_REQUEST)



class UI_acclist(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        ui_access=UI_access.objects.all()
        serializers=UI_accessSerializers(ui_access,many=True)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def post(self, request,format=None):
        data=JSONParser().parse(request)
        serializers=UI_accessSerializers(data=data['params'])
        if serializers.is_valid():
            serializers.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(content(types='error',message=serializers.errors),status=status.HTTP_400_BAD_REQUEST)

class UI_accDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return UI_access.objects.get(pk=pk)
        except UI_access.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ui_access = self.get_object(pk)
        serializer = UI_accessSerializers(ui_access)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        ui_access = self.get_object(pk)
        serializer = UI_accessSerializers(ui_access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ui_access = self.get_object(pk)
        ui_access.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)


class GetAccessList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,format=None):
        data = JSONParser().parse(request)
        uid=data['params']['uid']
        ui_access=UI_access.objects.filter(Users=uid)
        locker_access=Locker_access.objects.filter(Users=uid)
        UIserializers=UI_accessSerializers(ui_access,many=True)
        locker_accSerializers=Locker_accSerializers(locker_access,many=True)
        result={
            "UI":UI_accessSerializers.data,
            "locker":locker_accSerializers.data
        }
        return Response(result,status=status.HTTP_200_OK)