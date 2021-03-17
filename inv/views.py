from inv.models import Product,Stock
from inv.serializers import ProductSerializer,StockSerializer
from django.http import Http404

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from users.views import ProcessDataTools

stockRecord={
    "initial_value":"0",
    "out_value":"0",
    "in_value":"0",
    "Product_id":"",
    "remark":""
}

class Productlist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=request.data
        productSerializer = ProductSerializer(data=data)

        if productSerializer.is_valid():

            productSerializer.save()

            stockRecord.update({
                'initial_value': data.get('initial_value'),
                'Product_id': productSerializer.data['id'],
                'create_uid': data.get('create_uid'),
            })

        else:
            return Response(content(types='error',message=productSerializer.errors), status=status.HTTP_400_BAD_REQUEST)

        stockSerializer=StockSerializer(data=stockRecord)

        if stockSerializer.is_valid():
            stockSerializer.save()
            return Response(content(data=productSerializer.data), status=status.HTTP_201_CREATED)
        else:
            product=Product.objects.get(pk=productSerializer.data['id'])
            product.delete()

            return Response(content(types='error',message=productSerializer.errors), status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)
        return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_200_OK)

class Stocklist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = StockSerializer(data=data['params'])
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_201_CREATED)
        return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class StockDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(category)
        return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)
        return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stock = self.get_object(pk)
        stock.delete()
        return Response(content(types='success',message="the data has deleted"),status=status.HTTP_200_OK)

class Out_of_the_warehouse(APIView):



    def post(self, request,format=None):
        data=request.data
        # print(data.get('Pruduct_id'))
        
        stock=Stock.objects.filter(Product_id__exact=data.get('Product_id')).first()
        if stock is not None:

            stockRecord.update({
                "initial_value":stock.initial_value,
                "out_value":data.get('out_value'),
                "in_value":"0",
                "Product_id":data.get('Product_id'),
                "remark":data.get('remark'),
                "create_uid":data.get('create_uid')
            })

            serializer = StockSerializer(data=stockRecord)

            if serializer.is_valid():
                serializer.save()
                return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)
            return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class Enter_of_the_warehouse(APIView):

    def post(self, request,format=None):
        data=request.data
        # print(data.get('Pruduct_id'))
        stock=Stock.objects.filter(Product_id__exact=data.get('Product_id')).first()
        if stock is not None:
            stockRecord.update({
                "initial_value":stock.initial_value,
                "out_value":"0",
                "in_value":data.get('in_value'),
                "Product_id":data.get('Product_id'),
                "remark":data.get('remark'),
                "create_uid":data.get('create_uid')
            })

            serializer = StockSerializer(data=stockRecord)

            if serializer.is_valid():
                serializer.save()
                return Response(content(types='success',data=serializer.data), status=status.HTTP_200_OK)
            return Response(content(types='error',message=serializer.errors), status=status.HTTP_400_BAD_REQUEST)

class Current_quantity(APIView):

    def get(self, request, pk, format=None):
        # pk: procuct_id
        sql='SELECT id,initial_value,sum(in_value) AS in_value,sum(out_value) AS out_value FROM inv_stock WHERE Product_id_id={}'.format(pk)
        data={}
        stock=Stock.objects.raw(sql)
        for p in stock:
            data.update({
                'initial_value':p.initial_value,
                'out_value':p.out_value,
                'current_value':p.initial_value+p.in_value-p.out_value
            })

        return Response(content(types='success',data=data), status=status.HTTP_200_OK)

class Change_report(APIView):
    def post(self, request,format=None):
        pass

class search_product(APIView):
    def get(self, request,format=None):
        pass