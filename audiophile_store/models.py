from django.db import models
from datetime import date

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
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)
    description = models.CharField(max_length=255)
    Release_date = models.DateField(default= date.today)
    image = models.ForeignKey(Product_images, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    

    @property
    def order_cost(self):
        return 50

    @property
    def VAT(self):
        vat_rates = 0.2
        calculate_for_vat = ((self.price + self.order_cost) * vat_rates)/100
        return calculate_for_vat

    

# class 