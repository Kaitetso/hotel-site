from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('clients/', views.client_list, name='client_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
