from django.urls import path
from . import views

urlpatterns = [
    path('login', views.database, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('', views.paginaInicial, name='home'),
    path('produto/<int:id>', views.produto, name='produto'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('produtos', views.produtos, name='produtos'),
    path('sobre', views.sobre, name='sobre'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('trabalhe', views.trabalhe, name='trabalhe'),
    path('edita_perfil', views.edita_perfil, name='edita_perfil'),
    path('criar_usuario', views.criar_usuario),
    path('processar-cadastro', views.cadastrar_produto),
    path('adicionar_carrinho/<int:id>', views.adicionar_ao_carrinho),
    path('remover_carrinho/<int:id>', views.remover_carrinho),
]