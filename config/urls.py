from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ProductView, ConocenosView

urlpatterns = [

    path('api/', include('apps.user.urls')),
    path('api/', include('apps.product.urls')),
    path('api/', include('apps.cart.urls')),

    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductView.as_view(), name='product'),
    path('conocenos/', ConocenosView.as_view(), name='conocenos'),

]
