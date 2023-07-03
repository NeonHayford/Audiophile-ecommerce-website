# Generated by Django 4.1.5 on 2023-07-03 10:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='product_images/main/')),
                ('first_image', models.ImageField(upload_to='product_images/')),
                ('second_image', models.ImageField(upload_to='product_images/')),
                ('third_image', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=5)),
                ('description', models.CharField(max_length=255)),
                ('Release_date', models.DateField(default=datetime.date.today)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audiophile_store.category')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audiophile_store.product_images')),
            ],
        ),
    ]
