from rest_framework import serializers
from audiophile_store.models import  Cart, Cart_item, Customer_Address



class CartSerializer(serializers.ModelSerializer):
    cartid = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ('cartid',)


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_item
        fields = '__all__'
        # depth = 4


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Address
        fields = '__all__'

        