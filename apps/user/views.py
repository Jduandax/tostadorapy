from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializers


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        users = UserSerializers(users, many=True).data
        count = len(users)
        return Response(
            {
                "count": count,
                "users": users,
            }, status=status.HTTP_200_OK)


class UserDelete(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.filter(id=pk)
            user.delete()
            return Response('User delete', status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("User don't exist")


class Clientlogeado(APIView):
    def get(self, request):
        try:
            email = request.session['email']
            user = User.objects.get(email=email)
            user = UserSerializers(user).data
            return Response(user, status=status.HTTP_200_OK)
        except:
            return Response('No Hay clientes logeados', status=status.HTTP_400_BAD_REQUEST)


