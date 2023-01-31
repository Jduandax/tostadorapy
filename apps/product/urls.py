from django.urls import path
from .views import ListProduct, DeleteProduct, EditProduct, AddProduct, RegisterProduct

urlpatterns = [
    path('product/', ListProduct.as_view(), name='list_product'),
    path('delete/<int:pk>', DeleteProduct.as_view(), name='delete_product'),
    path('edit_product/<int:pk>', EditProduct.as_view(), name='edit_product'),
    path('add_product/<int:pk>/', AddProduct.as_view(), name='add_product'),
    path('register_product/', RegisterProduct.as_view(), name='register_product'),

]
