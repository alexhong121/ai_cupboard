from unit.models import Unit,Product_category
from unit.serializers import UnitSerializer,CategorySerializer
from django.http import Http404

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from utils.base import content

class Unitlist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        unit = Unit.objects.all()
        serializer = UnitSerializer(unit, many=True)
        return Response(content(types='success',data=serializer.data),status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # data = JSONParser().parse(request)
        serializer = UnitSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(content(types="success",data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class UnitDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Unit.objects.get(pk=pk)
        except Unit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        unit = self.get_object(pk)
        serializer = UnitSerializer(unit)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        unit = self.get_object(pk)
        serializer = UnitSerializer(unit, data=request.data["params"])
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

        return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        unit = self.get_object(pk)
        unit.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)

class Categorylist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        category = Product_category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Product_category.objects.get(pk=pk)
        except Product_category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data['params'])
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)
        return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_204_NO_CONTENT)