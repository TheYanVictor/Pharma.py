from django.db import models

class categoria_remedios(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)