from django.shortcuts import render
from rest_framework.views import APIView
from audiophile_store.models import cart, Cart_Add

# Create your views here.
# class CreateCartView(APIView):
#     def create(self, request):
#         item = Product.objects.get(id=request.data) 