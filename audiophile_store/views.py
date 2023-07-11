from rest_framework.views import APIView
from rest_framework.generics import  ListAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from .serializers import ProductSerializer, ProductImageSerializer, product_data
from .models import Product, Product_images
from drf_spectacular.utils import extend_schema

# Create your views here.
@extend_schema(request=ProductImageSerializer)
class ProductDataView(ListAPIView):
    serializer_class = ProductImageSerializer
    queryset = Product_images.objects.all()

# class ProductDataView(APIView):
#     def get(self, request, format=None):
#         product = Product.objects.all()
#         serializer=product_data(product, many=True)
#         return Response(serializer.data)
    

# Product Image
@extend_schema(request=ProductImageSerializer)
class CreateProductImageView(ListCreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = Product_images.objects.all()


@extend_schema(request=ProductImageSerializer)
class UpdateProductImageView(UpdateAPIView):
    serializer_class = ProductImageSerializer
    queryset = Product_images.objects.all()


#Product
@extend_schema(request=ProductSerializer)
class CreateProductView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@extend_schema(request=ProductSerializer)
class UpdateProductView(UpdateAPIView):
    serializer_class= ProductSerializer
    queryset=Product_images.objects.all()



class DeleteProductView(DestroyAPIView):
    serializer_class= ProductSerializer
    queryset=Product_images.objects.all()

# class DeleteProductView(APIView):
#     def get (self, request, pk):
#         try:
#             item = Product.objects.get(id=pk)
#             return Response(
#                         {
#                             'id': item.pk,
#                             'name': item.name,
#                             'price': item.price,
#                             'Release_date': item.Release_date,
#                         }
#                     )
#         except  Product.DoesNotExist:
#             return Response({'error': 'Product does not exist in the database'}, status=HTTP_204_NO_CONTENT)
    
#     def delete(self, request ,pk):
#         try:
#             item = Product.objects.get(id=pk)
#             if request.method == 'DELETE':
#                 if not item:
#                     return Response(status=HTTP_404_NOT_FOUND)
#                 else:
#                     item.delete()
#             return Response('Data successfully deleted', status=HTTP_204_NO_CONTENT)
#         except  Product.DoesNotExist:
#             return Response({'error': 'Product does not exist in the database'}, status=HTTP_204_NO_CONTENT)
