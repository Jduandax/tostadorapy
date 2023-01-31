from django.urls import path, include
from .models import Cart
from .views import CartDetail, CartUpdate, CartDelete, CreateCart



urlpatterns= [
    path('detail/<int:pk>', CartDetail.as_view()),
    path('actualizar/<int:pk>', CartUpdate.as_view()),
    path('borrar/<int:pk>', CartDelete.as_view()),
    path('create/',CreateCart.as_view())
]