from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from .serializers import CartSerializer, CartProductSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from audiophile_store.models import Cart, Cart_item

# Create your views here.
class CartView(APIView):
    def get(self, request):
        all_cart = Cart.objects.all()
        serializer = CartSerializer(all_cart,many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CartSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class DeleteCartView(APIView):
    def get (self, request, pk):
        try:
            item = Cart.objects.get(cart_add = pk)
            return Response(item.data)
        except  Cart.DoesNotExist:
            return Response({'error': 'Cart containing products add does not exist in the database'}, status=HTTP_204_NO_CONTENT)
    
    def delete(self, request ,pk):
        try:
            item = Cart.objects.get(cart_add= pk)
            if request.method == 'DELETE':
                if not item:
                    return Response(status=HTTP_404_NOT_FOUND)
                else:
                    item.delete()
            return Response('There is not cart-id created', status=HTTP_204_NO_CONTENT)
        except  Cart.DoesNotExist:
            return Response({'error': 'Cart does not exist...'}, status=HTTP_204_NO_CONTENT)

class CartProductView(ListAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()

class CreateCartProductView(ListCreateAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()

class UpdateCartProductView(UpdateAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()

class DeleteCartProductView(DestroyAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()


# class CartProductView(APIView):
#     def get(self, request):
#         try:
#             added_to_cart = Cart_item.objects.all()
#             print(added_to_cart)
#             serializer = CartProductSerializer(added_to_cart, many=True)
#             return Response(serializer.data)
#         except Cart_item.DoesNotExist:
#             return Response({'error': 'content does not exist'},status=HTTP_204_NO_CONTENT)
    
#     def post(self, request):
#         serializer = CartProductSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
