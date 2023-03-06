from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from apps.user.views import Clientlogeado


class HomeView(TemplateView):
    def get(self, request, **kwargs):
        user = Clientlogeado.get(self, request)
        if user.status_code == 200 and user.data["rol_id"] == 3:
            return render(request, 'catalogo.html', context=None)
        elif user.status_code == 200 and user.data["rol_id"] == 4:
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
        return render(request, 'admin.html', context=None)


class AyudaView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'ayuda.html', context=None)
