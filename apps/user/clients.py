from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Rol, Address
from .serializers import UserSerializers, RolSerializers, AddressSerializers
from utils import set_rol, send_email, recovery_password, send_email_discounts, get_name_role, send_email_address
import os, sys, django
from django.shortcuts import render, redirect
from django.contrib import messages


class Register(APIView):
    def get(self, request):
        cliente = User.objects.all()
        cliente = UserSerializers(cliente, many=True).data
        return render(request, 'register.html', {'cliente': cliente})

    def post(self, request):
        user = UserSerializers(data=request.data)
        if user.is_valid():
            user.save()
            user = User.objects.get(email=request.data['email'])
            set_rol(user)
            send_email(user)
            request.session['email'] = user.email
            messages.add_message(request, messages.SUCCESS, 'Usuario registrado correctamente')
            return redirect('list_product')
        else:
            messages.add_message(request, messages.ERROR, '!!!! El usuario ya existe !!!!')
            return redirect("register")


class Login(APIView):
    def get(self, request):
        cliente = User.objects.all()
        cliente = UserSerializers(cliente, many=True).data
        return render(request, 'login.html', {'cliente': cliente})

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        request.session['email'] = email
        try:
            rol = User.objects.get(email=email)
            rol = get_name_role(rol.rol_id_id)
            if rol != 'admin':
                cliente = User.objects.get(email=email)
                if cliente:
                    if password == cliente.password:
                        messages.add_message(request, messages.SUCCESS, f'Bienvenido Cliente {cliente.name}')
                        return redirect('list_product')
                    return Response('Password incorrect')
            else:
                admin = User.objects.get(email=email)
                if admin:
                    if password == admin.password:
                        messages.add_message(request, messages.SUCCESS, f'Bienvenido Administrador  {admin.name}')
                        return redirect('admin')
                    return Response('Password incorrect')
                else:
                    messages.add_message(request, messages.ERROR, f'El {email} no se encuentra registrado')
                    return Response('No existe')
        except:
            return Response('No existe')


class Logout(APIView):
    def post(self, request):
        del request.session['email']
        return Response('Logout success')


class EditProfile(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        user = UserSerializers(user, data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors)


class RecoveryPassword(APIView):
    def get(self, request):
        cliente = User.objects.all()
        cliente = UserSerializers(cliente, many=True).data
        return render(request, 'recovery.html', {'cliente': cliente})

    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email=email)
        recovery_password(user)
        messages.add_message(request, messages.SUCCESS, 'Se ha enviado un correo a su cuenta')
        return redirect('login')


class CreateAddress(APIView):
    def get(self, request):
        cliente = User.objects.all()
        cliente = UserSerializers(cliente, many=True).data
        return render(request, 'formulario_de_envio.html', {'cliente': cliente})

    def post(self, request):
        user = User.objects.get(email=request.session['email'])
        user_id = user.id
        address = AddressSerializers(data=request.data)
        if address.is_valid():
            address.save()
            address = Address.objects.last()
            address.user_id_id = user_id
            address.save()
            address = Address.objects.filter(user_id_id=user_id)
            print(address[0].direccion)
            messages.add_message(request, messages.SUCCESS, 'Datos de envio registrados correctamente')
            send_email_address(user, address)
            return render(request, 'formulario_de_envio.html',
                          {
                              'cliente': user,
                              'address': address
                          })
        else:
            messages.add_message(request, messages.ERROR, '!!!! La direccion ya existe !!!!')
            return redirect("createaddress")
