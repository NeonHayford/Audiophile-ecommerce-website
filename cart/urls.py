from django.urls import path
from .views import CartView

urlpatterns = [
    path('', CartView.as_view(), name='create_cart'),
    # path('', -----.as_view(), name=''),
]
