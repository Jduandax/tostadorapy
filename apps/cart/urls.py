from django.urls import path, include
from .views import CartDetail, CartUpdate, CartDelete, CreateCart, OrderDetail

urlpatterns = [
    path('detail/', CartDetail.as_view(), name='cart_detail'),
    path('actualizar/<int:pk>', CartUpdate.as_view(), name='cart_update'),
    path('borrar/<int:pk>', CartDelete.as_view(), name='cart_delete'),
    path('create/', CreateCart.as_view(), name='cart_create'),
    path('order/', OrderDetail.as_view(), name='order')
]
