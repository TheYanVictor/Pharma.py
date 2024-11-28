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
