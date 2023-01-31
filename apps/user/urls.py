from django.urls import path
from .views import UserList, UserDelete, Clientlogeado
from .clients import Register, Login, Logout, EditProfile, RecoveryPassword


urlpatterns = [
    path('user/', UserList.as_view(), name='user_list'),
    path('user/<int:pk>', UserDelete.as_view(), name='user_delete'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('clientlogeado/', Clientlogeado.as_view(), name='clientlogeado'),
    path('editprofile/<int:pk>', EditProfile.as_view(), name='editprofile'),
    path('recovery/', RecoveryPassword.as_view(), name='recovery'),

]
