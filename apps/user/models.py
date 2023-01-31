from django.db import models


# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta():
        db_table = 'tostadora_rol'


class User(models.Model):
    email = models.EmailField(max_length=150, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=200, null=False)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta():
        db_table = 'tostadora_user'
