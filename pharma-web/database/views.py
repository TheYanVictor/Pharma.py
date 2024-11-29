from django.shortcuts import render
from django.template import loader
from .models import clientes, categoria_remedios, medicamentos
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
    categorias_remedios = categoria_remedios.objects.all().values()
    medicamentos_oferta = medicamentos.objects.all()[:3].values()
    context = {
        'categorias': categorias_remedios,
        'produtos_amostra': medicamentos_oferta
    }
    return HttpResponse(template.render(context, request))

def produto(request, id):
    template = loader.get_template('produto.html')
    produto = medicamentos.objects.get(id=id)
    context = {
        'produto': produto
    }

    return HttpResponse(template.render(context, request))

def carrinho(request):
    template = loader.get_template('carrinho.html')

    return HttpResponse(template.render(request=request))


def produtos(request):
    template = loader.get_template('produtos.html')

    produtos = medicamentos.objects.all().values()
    context = {
        'produtos': produtos 
    }

    return HttpResponse(template.render(context, request))

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