from django.urls import path
from .views import CartView, CreateCartView, DeleteCartView, CartProductView, CreateCartProductView, UpdateCartProductView, DeleteCartProductView

urlpatterns = [
    # cart
    path('', CartView.as_view(), name='create_cart'),
    path('create', CreateCartView.as_view(), name='create_cart'),
    path('<str:pk>/delete', DeleteCartView.as_view(), name='delete_cart'), # the primary-key is the cartID
    # all product added to cart 
    path('cart-item', CartProductView.as_view(), name='get_item_from_cart'),
    path('delete-all/<str:pk>', DeleteCartProductView.as_view(), name='delete_all_items_from_cart'),
    # product added to cart 
    path('<str:cartid>/product', CreateCartProductView.as_view(), name='add_to_cart'),
    path('<str:cartid>/update/<str:pk>', UpdateCartProductView.as_view(), name='update_cart'),
    path('<str:cartid>/delete/product/<str:pk>', DeleteCartProductView.as_view(), name='delete_from_cart')
]
