from rest_framework.views import APIView
from rest_framework.generics import  CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from .serializers import ProductSerializer, ProductImageSerializer, product_data
from .models import Product, Product_images

# Create your views here.
class ProductDataView(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        print(product)
        serializer=product_data(product, many=True)

        return Response(serializer.data)

class CreateProductImageView(CreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = Product_images.objects.all()


class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class DeleteProductView(APIView):
    def get (self, request, pk):
        try:
            item = Product.objects.get(id=pk)
            return Response(
                        {
                            'id': item.pk,
                            'name': item.name,
                            'price': item.price,
                            'Release_date': item.Release_date,
                        }
                    )
        except  Product.DoesNotExist:
            return Response({'error': 'Product does not exist in the database'}, status=HTTP_204_NO_CONTENT)
    
    def delete(self, request ,pk):
        try:
            item = Product.objects.get(id=pk)
            if request.method == 'DELETE':
                if not item:
                    return Response(status=HTTP_404_NOT_FOUND)
                else:
                    item.delete()
            return Response('Data successfully deleted', status=HTTP_204_NO_CONTENT)
        except  Product.DoesNotExist:
            return Response({'error': 'Product does not exist in the database'}, status=HTTP_204_NO_CONTENT)
