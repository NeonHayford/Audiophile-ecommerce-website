from rest_framework import serializers
from .models import Product, Cart

class product_data(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth= 5


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cartid = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ('cartid',)



