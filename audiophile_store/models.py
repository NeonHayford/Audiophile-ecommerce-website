from django.db import models
from datetime import date
from uuid import uuid4
# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Product_images(models.Model):
    main_image = models.ImageField(upload_to='product_images/main/')
    first_image = models.ImageField(upload_to='product_images/')
    second_image = models.ImageField(upload_to='product_images/')
    third_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.main_image}'


class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=9999.99)
    description = models.CharField(max_length=255)
    Release_date = models.DateField(default= date.today)
    image = models.ForeignKey(Product_images, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    
class Cart(models.Model):
    cartid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    date = models.DateField(auto_now_add=True)


class Cart_Add(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


