from rest_framework import serializers
from .models import User, Rol


class UserSerializers(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'
