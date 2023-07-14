from rest_framework import serializers
from audiophile_store.models import Cart, Cart_item
from decimal import Decimal

class CartSerializer(serializers.ModelSerializer):
    cartid = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = Cart
        fields = ('cartid',)




class CartProductSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField('get_total_price_with_vat',  read_only=True)

    class Meta:
        model = Cart_item
        fields = '__all__'

    def get_total_amount(self, obj):
        # calculate the total cost of the items in the cart
        return sum(item.product.price * item.quantity  for item in Cart_item.objects.filter(cart = obj.cart))
    

    def get_vat_on_total_price(self, obj):
        # calculate VAT on the total cost of the items in the cart plus additional charges
        additional_price = sum(50 * item.quantity  for item in Cart_item.objects.filter(cart = obj.cart))
        VAT = self.get_total_amount(obj) * Decimal(0.20)
        return VAT + additional_price
    

    def get_total_price_with_vat(self, obj) -> str:
        # calculate VAT plus total cost of the items in the cart 
        return self.get_vat_on_total_price(obj) + self.get_total_amount(obj)


        