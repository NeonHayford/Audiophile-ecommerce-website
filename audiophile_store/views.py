from rest_framework.views import APIView
from rest_framework.generics import  CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from .serializers import ProductSerializer, product_data, CartSerializer
from .models import Product, Cart

# Create your views here.
class ProductDataView(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        print(product)
        serializer=product_data(product, many=True)

        return Response(serializer.data)


class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class DeleteProductView(APIView):
    def delete(self, request ,pk):
        item = Product.objects.get(id=pk)
        if not item:
            return Response(status=HTTP_404_NOT_FOUND)
        else:
            item.delete()
        return Response('Data successfully deleted', status=HTTP_204_NO_CONTENT)
