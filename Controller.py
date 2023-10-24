from Model import *  # Importa todas as classes do módulo Model
from Dao import *  # Importa todas as classes do módulo Dao
import random  # Importa o módulo random para gerar números aleatórios

class ControllerAdicionarTarefa():  # Define a classe ControllerAdicionarTarefa
    def __init__(self, tarefa):  # Método construtor que recebe a tarefa como parâmetro
        id = random.randint(1000, 9999)  # Gera um número aleatório entre 1000 e 9999 para o ID da tarefa
        self.id = int(id)  # Converte o ID para inteiro
        self.tarefa = tarefa  # Atribui a tarefa passada como parâmetro para a instância atual
        self.tarefa = f"{self.id} - {self.tarefa}"  # Formata a tarefa com o ID e o texto da tarefa
#?///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        if DAO.AdicionarTarefa(self.tarefa) == True:  # Se a tarefa foi adicionada com sucesso
            print("Tarefa Adicionada")  # Imprime uma mensagem de sucesso
        else:  # Se a tarefa não foi adicionada com sucesso
            print("Não foi possível adicionar a tarefa. Verifique o índice.")  # Imprime uma mensagem de erro

        


class ControllerExcluirTarefa:
    def __init__(self, excluir):
        self.excluir = int(excluir)
        self.excluir_tarefa()

    def excluir_tarefa(self):
        tarefas = DAO.listarTarefas()

        if self.excluir >= 1 and self.excluir <= len(tarefas):
            tarefa = tarefas[self.excluir - 1]
            tarefa_parts = tarefa.split(" - ", 1)

            if len(tarefa_parts) > 1:
                _, texto_tarefa = tarefa_parts
                print(f"Excluindo a tarefa: {texto_tarefa}")

                if DAO.ExcluirTarefa(self.excluir - 1):  # Correção: Chamada correta para DAO.ExcluirTarefa
                    print("Tarefa Excluída")
                else:
                    print("Não foi possível excluir a tarefa. Verifique o índice.")
            else:
                print("Tarefa não encontrada.")
        else:
            print("Índice inválido.")


class ControllerListarTarefas:  # Define a classe ControllerListarTarefas
    def __init__(self):  # Método construtor sem parâmetros
        self.lista = DAO.listarTarefas()  # Obtém a lista de todas as tarefas e atribui para a instância atual
        self.exibirTarefas()  # Chama o método exibirTarefas

    def exibirTarefas(self):   # Define o método exibirTarefas que imprime todas as tarefas na tela
        for i, tarefa in enumerate(self.lista):   # Para cada índice e tarefa na lista de tarefas
            tarefa_parts = tarefa.split(" - ", 1)   # Divide a tarefa em duas partes: ID e texto da tarefa
            if len(tarefa_parts) > 1:   # Se a tarefa foi dividida corretamente em duas partes
                numero_tarefa, texto_tarefa = tarefa_parts   # Obtém o ID e o texto da tarefa separadamente
                print(f"[{i + 1}] -> {texto_tarefa}")   # Imprime o índice (incrementado em 1) e o texto da tarefa
            else:   # Se a tarefa não foi dividida corretamente em duas partes
                print("Tarefa não encontrada.")
