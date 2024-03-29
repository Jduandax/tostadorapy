from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from apps.product.models import Product as Pr
from apps.user.models import User as Us
from apps.user.views import Clientlogeado


class HomeView(TemplateView):
    def get(self, request, **kwargs):
        user = Clientlogeado.get(self, request)
        if user.status_code == 200 and user.data["rol_id"] == 1:
            return redirect('list_product')
        elif user.status_code == 200 and user.data["rol_id"] == 2:
            return render(request, 'admin.html', context=None)
        else:
            return render(request, 'index.html', context=None)


class ProductView(TemplateView):
    def get(self, request, **kwargs):
        user = Clientlogeado.get(self, request)
        if user.status_code == 200:
            return redirect('list_product')
        else:
            return render(request, 'productos.html', context=None)


class ConocenosView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'aboutUs.html', context=None)


class AdminView(TemplateView):
    def get(self, request, **kwargs):
        user = Clientlogeado.get(self, request)
        name = user.data["name"]
        products = Pr.objects.all()
        count = Us.objects.count()
        count_product = Pr.objects.count()
        return render(request, 'admin.html',
                      {
                          'count': count,
                          'count_product': count_product,
                          'name': name,
                      })


class AyudaView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'ayuda.html', context=None)
