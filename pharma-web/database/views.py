from django.shortcuts import render, redirect
from django.template import loader
from .models import clientes, categoria_remedios, medicamentos, fornecedores, cart
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
    carro_pequeno = cart.objects.all()

    total = 0

    for x in carro_pequeno:
        total += x.total

    context = {
        'little_cart': carro_pequeno,
        'total': total
    }

    return HttpResponse(template.render(context, request))


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
    categorias = categoria_remedios.objects.all().values()
    context = {
        'categorias': categorias,
    }

    return HttpResponse(template.render(context, request))

def trabalhe(request):
    template = loader.get_template('trabalhe.html')

    return HttpResponse(template.render(request=request))

def edita_perfil(request):
    template = loader.get_template('edita_perfil.html')

    return HttpResponse(template.render(request=request))

def criar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if nome and email and senha:
            clientes.objects.create(nome=nome, email=email, senha=senha)
            return redirect('/')
        return HttpResponse("Missing something", status=400)
    return render(request, 'create_post.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        fabricante = request.POST['fabricante']
        preco = float(request.POST['preco'])
        estoque = int(request.POST['estoque'])
        data_validade = request.POST['data_validade']
        categoria_id = int(request.POST['categoria'])

        # Obtém a categoria associada
        categoria = categoria_remedios.objects.get(id=categoria_id)

        # Cria o novo medicamento
        novo_medicamento = medicamentos(
            nome=nome,
            descricao=descricao,
            fabricante=fabricante,
            preco=preco,
            estoque=estoque,
            data_validade=data_validade,
            categoria=categoria
        )
        novo_medicamento.save()

    categorias = categoria_remedios.objects.all()  # Lista de categorias para o dropdown
    return render(request, 'cadastrar.html', {'categorias': categorias})
    
def adicionar_ao_carrinho(request, id):
    medicamento = medicamentos.objects.get(id=id)
    preco = medicamento.preco

    # objeto = cart.objects.create(medicamento = id, quantidade = 1, preco_unitario = preco, total = preco)

    item, created = cart.objects.get_or_create(
        medicamento=medicamento,
        defaults={'quantidade': 1, 'preco_unitario': preco, 'total': preco}
    )
    if not created:
        item.quantidade += 1
        item.total = preco * item.quantidade
        item.save()
    return redirect('/produtos')

def remover_carrinho(request, id):
    objeto = cart.objects.get(id=id)

    if objeto:
        objeto.delete()
    return redirect('/carrinho')

