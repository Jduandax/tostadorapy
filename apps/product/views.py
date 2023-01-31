from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from apps.user.views import Clientlogeado
from apps.cart.models import Cart


class ListProduct(APIView):
    def get(self, request):
        product = Product.objects.all()
        product = ProductSerializer(product, many=True).data
        return render(request, 'catalogo.html', {'products': product})


def post(self, request):
    product = ProductSerializer(data=request.data)
    if product.is_valid():
        product.save()
        return Response(product.data, status=status.HTTP_200_OK)
    return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProduct(APIView):

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            if product:
                product.delete()
                return Response('Product eliminate')
        except:
            return Response('elimination failed')


class EditProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        product = ProductSerializer(product, data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data)
        return Response(product.errors)


class AddProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        cliente = Clientlogeado.get(self, request)
        cart = Cart.objects.filter(user_id=cliente.data['id'], product=product)
        if not cart:
            cart = Cart()
            cart.product = product
            cart.quantity = 1
            cart.user_id = cliente.data['id']
            cart.sub_total = product.price * cart.quantity
            cart.save()
            messages.add_message(request, messages.SUCCESS, 'Producto agregado al carrito')
            return redirect('list_product')
        else:
            cart = Cart.objects.get(user_id=cliente.data['id'], product=product)
            if cart.product_id == product.id:
                cart.quantity += 1
                cart.sub_total = product.price * cart.quantity
                cart.save()
                messages.add_message(request, messages.SUCCESS, 'Producto agregado al carrito')
                return redirect('list_product')
            else:
                cart = Cart()
                cart.product = product
                cart.quantity = 1
                cart.user_id = cliente.data['id']
                cart.sub_total = product.price * cart.quantity
                cart.save()
                messages.add_message(request, messages.SUCCESS, 'Producto agregado al carrito')
                return redirect('list_product')
