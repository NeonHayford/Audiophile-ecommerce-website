from rest_framework import serializers
from .models import Product, Product_images

class product_data(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth= 5

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_images
        fields = '__all__'
        verbose_name = 'Product image'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'





