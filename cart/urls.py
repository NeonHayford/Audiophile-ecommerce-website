from django.urls import path
from .views import CartView, DeleteCartView, CartProductView, CreateCartProductView, UpdateCartProductView, DeleteCartProductView, CustomerAddressView, CreateCustomerAddressView

urlpatterns = [
    path('', CartView.as_view(), name='create_cart'),
    path('<str:pk>/delete', DeleteCartView.as_view(), name='delete_cart'),

    path('cart-item', CartProductView.as_view(), name='get_item_from_cart'),
    path('delete/<str:cart_item>', DeleteCartProductView.as_view(), name='delete_all_items_from_cart'),

    path('<str:cartid>/product', CreateCartProductView.as_view(), name='add_to_cart'),
    path('<str:cartid>/update/<str:pk>', UpdateCartProductView.as_view(), name='update_cart'),
    path('<str:cartid>/delete/<str:pk>', DeleteCartProductView.as_view(), name='delete_from_cart'),
    # path('', -----.as_view(), name=''),

    path('customer', CustomerAddressView.as_view(), name='get_all_customer_address'),
    path('create/customer', CreateCustomerAddressView.as_view(), name='create_customer_address'),
    path('customer/<str:pk>/delete', DeleteCartProductView.as_view(), name='delete_customer_address'),

]
