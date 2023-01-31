from rest_framework import serializers
from .models import Product, Presentation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['presentation'] = instance.presentation.name
        return data


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = "__all__"
