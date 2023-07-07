
    /api/cart/4b36d3ddd2154a67a3db870c11c45903/product

    /api/cart/4b36d3ddd2154a67a3db870c11c45903/update/3




    class CartProductView(APIView):
        def get(self, request):
            try:
                added_to_cart = Cart_item.objects.all()
                print(added_to_cart)
                serializer = CartProductSerializer(added_to_cart, many=True)
                return Response(serializer.data)
            except Cart_item.DoesNotExist:
                return Response({'error': 'content does not exist'},status=HTTP_204_NO_CONTENT)
    
        def post(self, request):
            serializer = CartProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

    https://www.django-rest-framework.org/api-guide/pagination/


# features
  #### pagination