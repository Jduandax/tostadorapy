from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CartSerializer
from .models import Cart
from apps.product.views import ListProduct


class CartDetail(APIView):
    def get(self, request, pk):
        try:

            cart = Cart.objects.filter(id = pk)
            print(cart)
            cart = CartSerializer(cart, many=True).data
            return Response({ "cart": cart}, status=status.HTTP_200_OK)
        except:
            return Response("No found")


class CartUpdate(APIView):
    def get(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        cart = CartSerializer(cart, data=request.data)
        if cart.is_valid():
            cart.save()
            return Response(cart.data)
        return Response(cart.errors)


class CartDelete(APIView):
    def get(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
            if cart:
                cart.delete()
                return Response('Cart eliminate')
        except:
            return Response('elimination failed')


class CreateCart(APIView):
    def post(self, request):
        cart = CartSerializer(data=request.data)
        if cart.is_valid():
            cart.save()
            return Response(cart.data, status=status.HTTP_200_OK)
        return Response(cart.errors, status=status.HTTP_400_BAD_REQUEST)
