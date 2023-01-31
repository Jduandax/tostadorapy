from django.db import models


class Presentation(models.Model):
    name = models.CharField(max_length=100)

    class Meta():
        db_table = 'tostadora_product_presentation'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    picture = models.CharField(max_length=1000)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    stock = models.IntegerField()

    class Meta():
        db_table = 'tostadora_product'
