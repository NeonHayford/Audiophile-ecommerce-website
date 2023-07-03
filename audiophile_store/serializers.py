from rest_framework import serializers
from .models import Product

class product_data(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth= 5

# class ProductSerializer(serializers.ModelSerializer):
#     def add_product(request):
#         products = product_data

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = '__all__'
        fields= ('Category', 'name', 'price', 'description',)