from django.db import transaction
from django.shortcuts import render
from locker.models import Cabinet,Lockers
from locker.serializers import CabinetSerializer,LockersSerializer
from django.http import Http404

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from utils.base import content

# Create your views here.

lockerData={
    "location":"",
    "code":"",
    "name":"",
    "mode":"",
    "lock_time":0,
    "Cabinet":"",
    "status":False
}

class LockerTools():

    def initial(self,**kwargs):
        cabinet=Cabinet(name=kwargs['name'],row=kwargs['row'],column=kwargs['column'])
        cabinet.save()
        if cabinet is not None:
            for i in range(int(kwargs['row'])):
                for j in range(int(kwargs['column'])):
                    self._initial_locker(row=i+1,column=j+1,Cabinet_id=cabinet.id)
        

    def _initial_locker(self,**kwargs):
        location='{},{}'.format(kwargs['row'],kwargs['column'])
        lockers=Lockers(location=location,Cabinet_id=Cabinet.objects.get(pk=kwargs['Cabinet_id']))
        lockers.save()


class Cabinetlist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]
    def __init__(self):
        self._data=None
        self._errorsFlag=False
        self._serializerErrors=None


    def newLockers(self):
        cabinet=Cabinet.objects.get(pk=self._data)
        for column in range(cabinet.column):
            for row in range(cabinet.row):
                lockerData.update({
                    "location":"{0},{1}".format(column,row),
                    "Cabinet_id":self._data,
                })
                serializer= LockersSerializer(data=lockerData)
                if serializer.is_valid():
                    serializer.save()
                    self._errorsFlag=False
                else:
                    self._errorsFlag=True
                    self._serializerErrors=serializer.errors

    def get(self, request, format=None):
        cabinet = Cabinet.objects.all()
        serializer = CabinetSerializer(cabinet, many=True)
  
        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = CabinetSerializer(data=data['params'])
        if serializer.is_valid():
            serializer.save()
            self._data=serializer.data['id']
            transaction.on_commit(self.newLockers)
            if self._errorsFlag:
                return Response(content(types='error',message=self._serializerErrors), status=status.HTTP_400_BAD_REQUEST)
            return Response(content(types="success",message="the locker is created!"), status=status.HTTP_201_CREATED)
    
        return Response(content(types='error',message=serializer.errors),status=status.HTTP_400_BAD_REQUEST)


class CabinetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Cabinet.objects.get(pk=pk)
        except Cabinet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cabinet = self.get_object(pk)
        serializer = CabinetSerializer(cabinet)

        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        cabinet = self.get_object(pk)
        serializer = CabinetSerializer(cabinet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(content(types="success",data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(content(types='error',message=serializer.errors),status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cabinet = self.get_object(pk)
        cabinet.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)


class Lockerslist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        lockers = Lockers.objects.all()
        serializer = LockersSerializer(lockers, many=True)



        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = LockersSerializer(data=data['params'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(content(types='error',message=serializer.errors),status=status.HTTP_400_BAD_REQUEST)


class LockersDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Lockers.objects.get(pk=pk)
        except Lockers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lockers = self.get_object(pk)

        serializer = LockersSerializer(lockers)
        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        lockers = self.get_object(pk)
        serializer = LockersSerializer(lockers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)
        return Response(content(types='error',message=serializer.errors),status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        lockers = self.get_object(pk)
        lockers.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)