from django.urls import path, include
from .views import ProductDataView, CreateProductView, UpdateProductView, DeleteProductView, CreateProductImageView, UpdateProductImageView

urlpatterns = [
    # path('', ever, name=''),
    path('product', ProductDataView.as_view(), name='Product'),

    path('product/image', CreateProductImageView.as_view(), name='product_image'),
    path('product/image/<str:pk>', UpdateProductImageView.as_view(), name='product_image'),

    path('product/add', CreateProductView.as_view(), name='add_product'),
    path('product/<str:pk>/update', UpdateProductView.as_view(), name='add_product'),
    path('product/<str:pk>/remove', DeleteProductView.as_view(), name='remove_product'),

    path('cart/', include('cart.urls')),
]
