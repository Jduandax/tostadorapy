import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from apps.user.models import Rol
from constanst import ROLES


def validate_rol(name):
    rol = Rol.objects.filter(name=name).first()
    if rol:
        return True
    else:
        return False


def load_rol():
    for rol in ROLES:
        if not validate_rol(rol):
            Rol.objects.create(name=rol)
            print(f'Rol {rol} creado')
        else:
            print(f'Rol {rol} ya existe')


load_rol()
