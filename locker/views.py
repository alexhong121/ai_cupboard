from django.db import transaction
from django.shortcuts import render
from django.http import Http404
from locker.models import Cabinet,Lockers
from locker.serializers import CabinetSerializer,LockersSerializer
from locker.core import LockerTools

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from utils.base import content,DataFormat

# Create your views here.




class InitializeLockView(APIView):

    def get(self,request, format=None):
        lokerTools=LockerTools()
        
        result = lokerTools.initial()    
        return Response(result,status=status.HTTP_201_CREATED
        )


class Cabinetlist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        cabinet = Cabinet.objects.all()
        serializer = CabinetSerializer(cabinet, many=True)
  
        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = CabinetSerializer(data=data['params'])
        if serializer.is_valid():
            serializer.save()
            if self._errorsFlag:
                return Response(content(types='error'), status=status.HTTP_400_BAD_REQUEST)
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


class LockerslistView(APIView):
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