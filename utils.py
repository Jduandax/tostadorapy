import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.user.models import Rol, User
from django.core.mail import send_mail
from django.conf import settings
from apps.cart.models import Cart
from apps.product.models import Product


def set_rol(user):
    rol = Rol.objects.get(name='client')
    user.rol_id = rol
    user.save()


def send_email(user):
    subject = 'Bienvenido a la plataforma'
    message = f'Hola {user.name} , gracias por registrarte en nuestra plataforma'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def recovery_password(user):
    subject = 'Recuperacion de contraseña'
    message = f'Hola {user.name} , tu contraseña es: {user.password}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def send_email_discounts(user):
    subject = 'Descuentos'
    message = f'Hola {user.name} , tenemos descuentos para ti'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail(subject, message, email_from, recipient_list)


def get_name_role(id):
    rol = Rol.objects.get(id=id)
    return rol.name


def send_email_address(user, address):
    subject = 'Direccion de envio'
    message = f'Hola {user.name} , tu direccion de envio es: {address[0].direccion}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, os.environ.get('EMAIL_HOST_USER')]
    send_mail(subject, message, email_from, recipient_list)
