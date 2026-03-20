
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('concluir/<int:tarefa_id>/', views.concluir_tarefas, name='concluir_tarefa'),
    path('deletar/<int:tarefa_id>/', views.deletar_tarefas, name='deletar_tarefa')
]