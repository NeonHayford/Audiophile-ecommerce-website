from django.urls import path
from .views import ProductDataView, CreateProductView

urlpatterns = [
    # path('', ever, name=''),
    path('all', ProductDataView.as_view(), name='Product'),
    path('add', CreateProductView.as_view(), name='add_product'),
]
