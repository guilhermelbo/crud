from django.contrib import admin
from .models import Tarefa, Contato

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','descricao','ativo', 'contato_id','data_alteracao','data_cadastro')

admin.site.register(Tarefa, TarefaAdmin)

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','data_alteracao','data_cadastro')

admin.site.register(Contato, ContatoAdmin)


