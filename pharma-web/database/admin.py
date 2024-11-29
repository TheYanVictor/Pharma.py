from django.contrib import admin
from .models import categoria_remedios, clientes, fornecedores, funcionarios, medicamentos, compras, itens_compra, vendas, itens_venda


# Register your models here.
admin.site.register(categoria_remedios)
admin.site.register(clientes)
admin.site.register(fornecedores)
admin.site.register(funcionarios)
admin.site.register(medicamentos)
admin.site.register(compras)
admin.site.register(itens_compra)
admin.site.register(vendas)
admin.site.register(itens_venda)