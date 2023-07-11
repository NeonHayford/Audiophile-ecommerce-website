from django.db import models
from uuid import uuid4

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

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
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=9999.99)
    features = models.TextField(blank =True, default='product features description...')
    description = models.TextField(blank = True, default='product description...')
    Release_date = models.DateField(auto_now=True)
    image = models.ForeignKey(Product_images, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    
class Cart(models.Model):
    cartid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    date = models.DateField(auto_now_add=True)
    

class Cart_item(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products')
    created = models.DateField(auto_now=True)
    modified = models.DateField(auto_now_add=True)


