from django.db import models

class categoria_remedios(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

class clientes(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)


class fornecedores(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)


class funcionarios(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    salario = models.FloatField()
    data_admissao = models.DateField()

class medicamentos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=50)
    preco = models.FloatField()
    estoque = models.IntegerField()
    data_validade = models.DateField()
    categoria = models.ForeignKey(categoria_remedios, on_delete=models.CASCADE)


class compras(models.Model):
    data_compra = models.DateField()
    valor_total = models.FloatField()
    id_fornecedor = models.ForeignKey(fornecedores, on_delete=models.CASCADE)



class itens_compra(models.Model):
    quantidade = models.IntegerField()
    preco_unitario = models.FloatField()
    id_compra = models.ForeignKey(compras, on_delete=models.CASCADE)
    id_medicamento = models.ForeignKey(medicamentos, on_delete=models.CASCADE)


class vendas(models.Model):
    data_venda = models.DateField()
    valor_total = models.FloatField()
    id_cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)
    id_funcionario = models.ForeignKey(funcionarios, on_delete=models.CASCADE)


class itens_venda(models.Model):
    quantidade = models.IntegerField()
    preco_unitario = models.FloatField()
    id_medicamento = models.ForeignKey(medicamentos, on_delete=models.CASCADE)
    id_vendas = models.ForeignKey(vendas, on_delete=models.CASCADE)
