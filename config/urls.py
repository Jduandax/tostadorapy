from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ProductView, ConocenosView, AdminView

urlpatterns = [

    path('api/', include('apps.user.urls')),
    path('api/', include('apps.product.urls')),
    path('api/', include('apps.cart.urls')),

    path('', HomeView.as_view(), name='home'),
    path('product/', ProductView.as_view(), name='product'),
    path('conocenos/', ConocenosView.as_view(), name='conocenos'),
    path('admin/', AdminView.as_view(), name='admin'),

]
