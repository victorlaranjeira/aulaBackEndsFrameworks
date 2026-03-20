from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

# Create your views here.
def listar_tarefas(request):

    if request.method == "POST":
        texto_digitado = request.POST.get('novo_titulo')
        Tarefa.objects.create(titulo = texto_digitado)
        return redirect('listar_tarefas')
    


    minhas_tarefas = Tarefa.objects.all()
    return render(request, 'tarefas.html', {'tarefas': minhas_tarefas})

def concluir_tarefas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('listar_tarefas')

def deletar_tarefas(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    return redirect('listar_tarefas')
