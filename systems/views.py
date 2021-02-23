from django.shortcuts import render
from django.http import Http404
from systems.models import Information,Configuration
from systems.serializers import ConfigSerializer,InformationSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from utils.base import content

# Create your views here.

class Configlist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        configuration = Configuration.objects.all()
        serializer = ConfigSerializer(configuration, many=True)
        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # data = JSONParser().parse(request)
        serializer = ConfigSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(types='error',message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfigDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Configuration.objects.get(pk=pk)
        except Configuration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        configuration = self.get_object(pk)
        serializer = ConfigSerializer(configuration)
        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        configuration = self.get_object(pk)
        serializer = ConfigSerializer(configuration, data=request.data["params"])
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)
        return Response(types='error',message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        configuration = self.get_object(pk)
        configuration.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)

class Informationlist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        information = Information.objects.all()
        serializer = InformationSerializer(information, many=True)
        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # data = JSONParser().parse(request)
        serializer = InformationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(types='error',message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InformationDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Information.objects.get(pk=pk)
        except Information.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        information = self.get_object(pk)
        serializer = InformationSerializer(information)
        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        information = self.get_object(pk)
        serializer = InformationSerializer(information, data=request.data["params"])
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(types='error',message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        information = self.get_object(pk)
        information.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)