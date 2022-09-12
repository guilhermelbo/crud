from rest_framework import serializers
from .models import Tarefa, Contato

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class TarefaSerializer(serializers.ModelSerializer):
    contato = ContatoSerializer(read_only=True)

    class Meta:
        model = Tarefa
        fields = ('id','titulo','descricao','ativo','data_alteracao','data_cadastro','contato')

