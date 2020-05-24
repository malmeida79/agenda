from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null = True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao =models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Nome que desejop que a tabela tenha (pode n ser informado)
    class Meta:
        db_table = 'evento'

    # as linhas abaixo server para definir qual campo deve aparecer
    # na listagem de pesquisa
    def __str__(self):
        return self.titulo