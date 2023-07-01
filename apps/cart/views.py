from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CartSerializer, OrderSerializer
from .models import Cart, Order
from apps.product.views import ListProduct
from apps.user.views import Clientlogeado


class CartDetail(APIView):
    def get(self, request):
        user = Clientlogeado.get(self, request)
        user_id = (user.data['id'])
        cart = Cart.objects.filter(user_id=user_id)
        cart = CartSerializer(cart, many=True).data
        return render(request, 'cart.html', {'cart': cart})


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


class OrderDetail(APIView):

    def get(self, request):
        user = Clientlogeado.get(self, request)
        user_id = (user.data['id'])
        order = Order.objects.filter(user_id=user_id)
        order = OrderSerializer(order, many=True).data
        return render(request, 'ordenCompra.html', {'order': order})
