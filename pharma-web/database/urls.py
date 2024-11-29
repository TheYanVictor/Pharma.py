from django.urls import path
from . import views

urlpatterns = [
    path('login', views.database, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('home', views.paginaInicial, name='home'),
    path('produto', views.produto, name='produto'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('produtos', views.produtos, name='produtos'),
    path('sobre', views.sobre, name='sobre'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('trabalhe', views.trabalhe, name='trabalhe'),
    path('edita_perfil', views.edita_perfil, name='edita_perfil'),
]