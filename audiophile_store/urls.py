from django.urls import path, include
from .views import ProductDataView, CreateProductView, UpdateProductView, DeleteProductView, CreateProductImageView, UpdateProductImageView

urlpatterns = [
    # product images
    path('product/image', ProductDataView.as_view(), name='Product'),
    path('product/create/image', CreateProductImageView.as_view(), name='product_image'),
    path('product/image/<str:id>', UpdateProductImageView.as_view(), name='product_image'),
    # products
    
    path('product/create', CreateProductView.as_view(), name='add_product'),
    path('product/<str:pk>/update', UpdateProductView.as_view(), name='add_product'),
    path('product/<str:pk>/remove', DeleteProductView.as_view(), name='remove_product'),

    path('cart/', include('cart.urls')),
]
