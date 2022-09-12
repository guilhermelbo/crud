from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tarefa, Contato
from .serializers import TarefaSerializer, ContatoSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_tarefas(request):
    tarefas = [tarefa.as_dict() for tarefa in Tarefa.objects.all().order_by('-id')]
    serializer = TarefaSerializer(tarefas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def nova_tarefa(request):
    serializer = TarefaSerializer(data=request.data)
    if serializer.is_valid():
        contato = Contato.objects.filter(id=request.data['contato_id'])
        if contato:
            serializer.save(contato_id=contato[0])
        else:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualiza_tarefa(request):
    try:
        tarefa = Tarefa.objects.get(id=request.data['id'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TarefaSerializer(tarefa, data=request.data)
    if serializer.is_valid():
        contato = Contato.objects.filter(id=request.data['contato_id'])
        if contato:
            serializer.save(contato_id=contato[0])
        else:
            serializer.save(contato_id=None)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleta_tarefa(request, pk):
    try:
        tarefa = Tarefa.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    tarefa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_contatos(request):
    contatos = Contato.objects.all().order_by('-id')
    serializer = ContatoSerializer(contatos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def novo_contato(request):
    serializer = ContatoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualiza_contato(request):
    try:
        contato = Contato.objects.get(id=request.data['id'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ContatoSerializer(contato, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleta_contato(request, pk):
    try:
        contato = Contato.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    contato.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
