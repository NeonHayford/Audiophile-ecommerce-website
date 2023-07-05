from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CartSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.core.exceptions import ValidationError
from audiophile_store.models import Cart, Cart_Add

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
    
    # def delete(self, request):
    #     cart = Cart.objects.get()
    #     if cart:
    #         cart.delete()
    #     else:
    #         return Response(status=HTTP_404_NOT_FOUND)
    

class AddProductCart(APIView):
    pass
    
