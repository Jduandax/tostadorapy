from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0, null=True, blank=True)
    picture = models.CharField(max_length=1000)
    presentation = models.CharField(max_length=1000)
    stock = models.IntegerField()

    class Meta():
        db_table = 'tostadora_product'
