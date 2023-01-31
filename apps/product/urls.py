from django.urls import path
from .views import ListProduct, DeleteProduct, EditProduct, AddProduct
from .presentation import PresentationList, EditPresentation

urlpatterns = [
    path('product/', ListProduct.as_view(), name='list_product'),
    path('delete/<int:pk>', DeleteProduct.as_view()),
    path('edit_product/<int:pk>', EditProduct.as_view()),
    path('presentation/', PresentationList.as_view()),
    path("edit_presentation/<int:pk>", EditPresentation.as_view()),
    path('add_product/<int:pk>/', AddProduct.as_view(), name='add_product'),

]
