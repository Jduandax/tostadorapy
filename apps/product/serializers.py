from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def get_price(self, obj):
        return '{:,.2f}'.format(obj.price).replace(',', '.')

    # def validate(self, data):
    #     product = Product.objects.filter(name=data['name'])
    #     if product:
    #         raise serializers.ValidationError('El producto ya existe')
    #     return data

    def create(self, validated_data):
        presentation = validated_data['presentation']
        if presentation == '20 Kg':
            validated_data['price'] = 22300
        elif presentation == '10 Kg':
            validated_data['price'] = 11200
        elif presentation == '5 Kg':
            validated_data['price'] = 5600
        elif presentation == '30 Kg':
            validated_data['price'] = 33500
        elif presentation == '40 Kg':
            validated_data['price'] = 44800
        elif presentation == '50 Kg':
            validated_data['price'] = 56000
        elif presentation == '60 Kg':
            validated_data['price'] = 67200
        elif presentation == '70 Kg':
            validated_data['price'] = 78400
        elif presentation == '80 Kg':
            validated_data['price'] = 89600
        elif presentation == '90 Kg':
            validated_data['price'] = 100800
        elif presentation == '100 Kg':
            validated_data['price'] = 112000
        return Product.objects.create(**validated_data)

    def save(self, *args, **kwargs):
        category_name = self.validated_data['category_name']
        category = Category.objects.filter(name=category_name)
        if category:
            self.validated_data['category'] = category[0]
        else:
            category = Category.objects.create(name=category_name)
            self.validated_data['category'] = category
        super(ProductSerializer, self).save(*args, **kwargs)




