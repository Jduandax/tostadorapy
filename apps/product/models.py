from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta():
        db_table = 'tostadora_category'


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    picture = models.CharField(max_length=1000)
    presentation = models.CharField(max_length=1000)
    stock = models.IntegerField()
    category_name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta():
        db_table = 'tostadora_product'

    def save(self, *args, **kwargs):
        self.name = self.category.name
        super(Product, self).save(*args, **kwargs)
