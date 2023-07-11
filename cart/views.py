from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from .serializers import CartSerializer, CartProductSerializer 
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from audiophile_store.models import Cart, Cart_item 
from drf_spectacular.utils import extend_schema, OpenApiParameter


# Create your views here.
@extend_schema(request=CartSerializer)
class CartView(ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


@extend_schema(request=CartSerializer)
class CreateCartView(ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    
# class CreateCartView(APIView):
#     def get(self, request):
#         all_cart = Cart.objects.all()
#         serializer = CartSerializer(all_cart,many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         serializer = CartSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

@extend_schema(request=CartSerializer)
class DeleteCartView(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# class DeleteCartView(APIView):
#     def get (self, request, pk):
#         try:
#             item = Cart.objects.get(cartid = pk)
#             return Response(item.data)
#         except  Cart.DoesNotExist:
#             return Response({'error': 'Cart containing products add does not exist in the database'}, status=HTTP_204_NO_CONTENT)
    
#     def delete(self, request ,pk):
#         try:
#             item = Cart.objects.get(cartid= pk)
#             if request.method == 'DELETE':
#                 if not item:
#                     return Response(status=HTTP_404_NOT_FOUND)
#                 else:
#                     item.delete()
#             return Response('There is not cart-id created', status=HTTP_204_NO_CONTENT)
#         except  Cart.DoesNotExist:
#             return Response({'error': 'Cart does not exist...'}, status=HTTP_204_NO_CONTENT)


@extend_schema(request=CartProductSerializer)
class CartProductView(ListAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()


@extend_schema(request=CartProductSerializer)
# , parameters=[OpenApiParameter(name="totalPrice", required=True,type = str)]
class CreateCartProductView(ListCreateAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()


@extend_schema(request=CartProductSerializer)
class UpdateCartProductView(UpdateAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()


@extend_schema(request=CartProductSerializer)
class DeleteCartProductView(DestroyAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()

