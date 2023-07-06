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
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    modified = models.DateField(auto_now_add=True)


class Customer_Address(models.Model):
    # Billing Details
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150) # create validatior
    phone = models.CharField(max_length=12, verbose_name='Phone Number') # create validatior
    # Shipping Info
    Address = models.CharField(max_length=100)
    Zip_code = models.CharField(max_length=6, verbose_name='Zip Code') # create validatior
    City = models.CharField(max_length=34)
    Country = models.CharField(max_length=50)


class Payment_detail(models.Model):
    customer = models.ForeignKey(Customer_Address, on_delete=models.CASCADE)
    e_money_number = models.CharField(max_length=12, verbose_name='e-Money Number') # validatior
    e_money_pin = models.CharField(max_length=4, verbose_name='e-Money PIN') # create validatior

