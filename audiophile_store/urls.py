from django.urls import path, include
from .views import ProductDataView, CreateProductView, DeleteProductView, CreateProductImageView

urlpatterns = [
    # path('', ever, name=''),
    path('product', ProductDataView.as_view(), name='Product'),
    path('product/image', CreateProductImageView.as_view(), name='product_image'),
    path('product/add', CreateProductView.as_view(), name='add_product'),
    path('product/remove/<str:pk>', DeleteProductView.as_view(), name='remove_product'),
    path('cart/', include('cart.urls')),
]
