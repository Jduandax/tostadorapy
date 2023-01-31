from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ProductView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'productos.html', context=None)


class ConocenosView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'aboutUs.html', context=None)
