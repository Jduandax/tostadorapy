from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from apps.user.views import Clientlogeado
from apps.cart.models import Cart, Order
from django.http import HttpResponseRedirect


class ListProduct(APIView):
    def get(self, request):
        product = Product.objects.all()
        product = ProductSerializer(product, many=True).data
        user = Clientlogeado.get(self, request)
        user_id = (user.data['id'])
        cart = Cart.objects.filter(user_id=user_id)
        return render(request, 'catalogo.html',
                      {
                          'products': product,
                          'cart': cart

                      })


class RegisterProduct(APIView):
    def get(self, request):
        products = Product.objects.all()
        products = ProductSerializer(products, many=True).data
        return render(request, 'registrar_producto.html', {'products': products})

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return redirect('register_product')
        else:
            messages.add_message(request, messages.ERROR, 'El Producto ya existe')
            return redirect('register_product')


class DeleteProduct(APIView):

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            if product:
                product.delete()
                return redirect('register_product')
        except:
            return Response('elimination failed')


class EditProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        product = ProductSerializer(product).data
        return render(request, 'edit_producto.html', {'product': product})

    def post(self, request, pk):
        producto = Product.objects.get(pk=pk)
        product = ProductSerializer(producto, data=request.data)
        if product.is_valid():
            product.save()
            return redirect('register_product')
        else:
            return Response(
                product.errors,
                status=status.HTTP_400_BAD_REQUEST)


class AddProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        cliente = Clientlogeado.get(self, request)
        cart = Cart.objects.filter(user_id=cliente.data['id'])
        # si no tiene carrito se crea uno
        if not cart:
            print('no tiene carrito')
            cart = Cart()
            cart.product = product
            cart.quantity = 1
            cart.user_id = cliente.data['id']
            cart.sub_total = product.price * cart.quantity
            cart.save()
            order = Order()
            order.user_id = cliente.data['id']
            order.cart_id = cart.id
            order.total = product.price * cart.quantity
            order.total_quantity = cart.quantity
            order.save()
            messages.add_message(request, messages.SUCCESS, f'Producto {product.name} agregado al carrito')
            return redirect('list_product')
        elif cart:
            print("si tiene carrito")
            for c in cart:
                if c.product_id == product.id:
                    print("si tiene carrito, y es el mismo producto")
                    cart = Cart.objects.get(user_id=cliente.data['id'], product=product)
                    cart.quantity += 1
                    cart.sub_total = product.price * cart.quantity
                    cart.save()
                    order = Order.objects.get(user_id=cliente.data['id'], cart_id=cart.id)
                    order.total = cart.sub_total
                    order.total_quantity = cart.quantity
                    order.save()
                    messages.add_message(request, messages.SUCCESS, f'Producto {product.name} agregado al carrito')
                    return redirect('list_product')
                else:
                    print("tiene carrito pero es otro producto")
                    cart = Cart()
                    cart.product = product
                    cart.quantity = 1
                    cart.user_id = cliente.data['id']
                    cart.sub_total = product.price * cart.quantity
                    cart.save()
                    order = Order.objects.get(user_id=cliente.data['id'])
                    order.total = order.total + cart.sub_total
                    order.total_quantity = order.total_quantity + cart.quantity
                    order.save()
                    messages.add_message(request, messages.SUCCESS, f'Producto {product.name} agregado al carrito')
                    return redirect('list_product')


class ProductCartList(APIView):
    def get(self, request):
        cliente = Clientlogeado.get(self, request)
        carts = Cart.objects.filter(user_id=cliente.data['id'])
        order = Order.objects.filter(user_id=cliente.data['id'])
        products = []
        for cart in carts:
            product = Product.objects.get(pk=cart.product_id)
            products.append(product)
        return render(request, 'cart.html', {
            'products': products,
            'carts': carts, 'order': order})
        # else:
        #     messages.add_message(request, messages.ERROR, 'No tienes productos en el carrito')
        #     return redirect('list_product')


class DeleteProductCart(APIView):
    def get(self, request, pk):
        cliente = Clientlogeado.get(self, request)
        cart = Cart.objects.get(pk=pk)
        cart.quantity -= 1
        if cart.quantity == 0:
            cart.delete()
            messages.add_message(request, messages.SUCCESS, f'Producto {cart.product.name} eliminado del carrito')
            return redirect('product_cart')
        cart.sub_total = cart.product.price * cart.quantity
        cart.save()
        order = Order.objects.get(user_id=cliente.data['id'])
        order.total = order.total - cart.product.price
        order.total_quantity = order.total_quantity - 1
        order.save()
        if order.total_quantity == 0:
            cart.delete()
            messages.add_message(request, messages.SUCCESS, f'Producto {cart.product.name} eliminado del carrito')
            return redirect('list_product')
        else:
            messages.add_message(request, messages.SUCCESS, f'Producto {cart.product.name} eliminado del carrito')
            return redirect('product_cart')
