from django.shortcuts import render
from django.template import loader
from .models import clientes
from django.http import HttpResponse


# Create your views here.
def database(request):
    clientes_login = clientes.objects.all().values()
    template = loader.get_template('login.html')
    context = {
        'clientes': clientes_login,
    }

    return HttpResponse(template.render(context, request))

def cadastro(request):
    template = loader.get_template('cadastro.html')

    return HttpResponse(template.render(request=request))

def paginaInicial(request):
    template = loader.get_template('pagina_inicial.html')
    
    return HttpResponse(template.render(request=request))

def produto(request):
    template = loader.get_template('produto.html')

    return HttpResponse(template.render(request=request))

def carrinho(request):
    template = loader.get_template('carrinho.html')

    return HttpResponse(template.render(request=request))


def produtos(request):
    template = loader.get_template('produtos.html')

    return HttpResponse(template.render(request=request))

def sobre(request):
    template = loader.get_template('sobre.html')

    return HttpResponse(template.render(request=request))

def cadastrar(request):
    template = loader.get_template('cadastrar.html')

    return HttpResponse(template.render(request=request))

def trabalhe(request):
    template = loader.get_template('trabalhe.html')

    return HttpResponse(template.render(request=request))

def edita_perfil(request):
    template = loader.get_template('edita_perfil.html')

    return HttpResponse(template.render(request=request))