from rest_framework import serializers
from .models import User, Rol, Address


class UserSerializers(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'


class RolSerializers(serializers.ModelSerializer):
    class Meta():
        model = Rol
        fields = '__all__'


class AddressSerializers(serializers.ModelSerializer):
    class Meta():
        model = Address
        fields = '__all__'

    #asignarle el user_id al address, el que esta logueado

