from rest_framework import serializers
from audiophile_store.models import  Cart, Cart_Add


class CartSerializer(serializers.ModelSerializer):
    cartid = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ('cartid',)