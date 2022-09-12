from django.urls import path
from .views import *

urlpatterns = [
    path('tarefas/', get_tarefas),
    path('tarefas/nova-tarefa/', nova_tarefa),
    path('tarefas/atualiza-tarefa/', atualiza_tarefa),
    path('tarefas/deleta-tarefa/<int:pk>/', deleta_tarefa),
    path('contatos/', get_contatos),
    path('contatos/novo-contato/', novo_contato),
    path('contatos/atualiza-contato/', atualiza_contato),
    path('contatos/deleta-contato/<int:pk>/', deleta_contato)
]
