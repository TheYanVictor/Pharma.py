from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.database, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.paginaInicial, name='home')
]