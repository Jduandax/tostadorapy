import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.user.models import Rol, User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from apps.cart.models import Cart, Order
from apps.product.models import Product
from django.core.mail import EmailMultiAlternatives
from datetime import datetime


def set_rol(user):
    rol = Rol.objects.get(name='client')
    user.rol_id = rol
    user.save()


def send_email(user):
    subject = 'Bienvenido a la plataforma'
    template = "../templates/email.html"

    context = {'user': user}
    html_content = render_to_string(template, context)

    text_content = f'Bienvenido(a) a nuestra plataforma, {user.name}! Gracias por registrarte.'

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [user.email])

    msg.attach_alternative(html_content, "text/html")

    # Envía el correo electrónico
    msg.send()


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
    subject = 'Gracias por tu compra'
    template = "../templates/envio.html"

    now = datetime.now()
    latest_order = Order.objects.filter(user_id=user.id).last()
    total = latest_order.total

    cart_items = Cart.objects.filter(user=user).select_related('product')



    context = {
        'user': user,
        'address': address[0],
        'fecha': now.strftime("%d/%m/%Y %H:%M:%S"),
        'total': total,
        'cart_items': cart_items,
        'orden': latest_order.id,

    }

    html_content = render_to_string(template, context)

    text_content = f'Hola {user.name}, ' \
                   f'gracias por tu compra. Pronto estaremos enviando tu pedido a esta dirección: ' \
                   f'{address[0].direccion}'

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [user.email])

    msg.attach_alternative(html_content, "text/html")

    # Envía el correo electrónico
    msg.send()

