from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, product_data
from .models import *
from rest_framework.serializers import ValidationError
# from django.http import Http404
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.decorators import api_view

# Create your views here.
class ProductDataView(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        print(product)
        serializer=product_data(product, many=True)

        return Response(serializer.data)


# @api_view(['POST'])
# def add_product(request):
#     item = ProductSerializer(data=request.data)
#     # if Product.objects.filter(id=item.id).exists():
#     #     return ValidationError('Product already exists')
#     if item.is_valid():
#         item.save()
#     else:
#         # return Http404
#         return Response({'error': 'you did not enter the product Credientials...'}, status = HTTP_404_NOT_FOUND)
class CreateProductView(APIView):
    def post(self, request):
        item = ProductSerializer(data=request.data)
        # if Product.objects.filter(id=item.id).exists():
        #     return ValidationError('Product already exists')
        if item.is_valid():
            product = item.save() 
            print(product)
            return Response(
                {
                    "id": product.id,
                    'name': product.name,
                    'description': product.description,
                    'Release_date': product.Release_date
                },
                status = HTTP_200_OK
            )
        else:
            # return Http404
            return Response({'error': 'you did not enter the product Credientials...'}, status = HTTP_404_NOT_FOUND)
        
        
    # def delete(self, request):
