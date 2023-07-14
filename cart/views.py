from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from .serializers import CartSerializer, CartProductSerializer 
from audiophile_store.models import Cart, Cart_item 
from drf_spectacular.utils import extend_schema


# Create your views here.
@extend_schema(request=CartSerializer)
class CartView(ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


@extend_schema(request=CartSerializer)
class CreateCartView(ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


@extend_schema(request=CartSerializer)
class DeleteCartView(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


@extend_schema(request=CartProductSerializer)
class CartProductView(ListAPIView):
    serializer_class = CartProductSerializer
    queryset = Cart_item.objects.all()


@extend_schema(request=CartProductSerializer)
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

