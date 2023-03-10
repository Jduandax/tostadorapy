from django.db import models
from apps.product.models import Product
from apps.user.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    sub_total = models.IntegerField(default=0)

    def __str__(self):
        return "Carrito de: " + self.user.name

    class Meta():
        db_table = 'tostadora_cart'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    total_quantity = models.IntegerField(default=0)

    def __str__(self):
        return "Orden de: " + self.user.name

    class Meta():
        db_table = 'tostadora_order'
