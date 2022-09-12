from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50) 
    data_alteracao = models.DateTimeField(auto_now=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    ativo = models.BooleanField(default=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    contato_id = models.ForeignKey(Contato, null=True, on_delete=models.SET_NULL, blank=True)
    
    def as_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo, 
            'descricao': self.descricao,
            'ativo': self.ativo,
            'data_alteracao': self.data_alteracao,
            'data_cadastro': self.data_cadastro,
            'contato': self.contato_id
        }