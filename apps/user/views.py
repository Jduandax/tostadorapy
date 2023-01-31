from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializers
from django.shortcuts import render, redirect


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        users = UserSerializers(users, many=True).data
        return render(request, 'listar_usuarios.html', {'users': users})



class UserDelete(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.filter(id=pk)
            user.delete()
            return redirect('user_list')
        except:
            return Response('No se pudo eliminar el usuario', status=status.HTTP_400_BAD_REQUEST)


class Clientlogeado(APIView):
    def get(self, request):
        try:
            email = request.session['email']
            user = User.objects.get(email=email)
            user = UserSerializers(user).data
            return Response(user, status=status.HTTP_200_OK)
        except:
            return Response('No Hay clientes logeados', status=status.HTTP_400_BAD_REQUEST)


