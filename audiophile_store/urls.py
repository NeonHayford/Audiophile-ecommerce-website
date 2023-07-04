from django.urls import path, include
from .views import ProductDataView, CreateProductView, DeleteProductView

urlpatterns = [
    # path('', ever, name=''),
    path('product', ProductDataView.as_view(), name='Product'),
    path('add', CreateProductView.as_view(), name='add_product'),
    path('remove/<str:pk>', DeleteProductView.as_view(), name='remove_product'),
    path('cart', include('cart.urls')),
]
