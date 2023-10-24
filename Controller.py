from Model import *  # Importa todas as classes do módulo Model
from Dao import *  # Importa todas as classes do módulo Dao
import random  # Importa o módulo random para gerar números aleatórios

class ControllerAdicionarTarefa():  # Define a classe ControllerAdicionarTarefa
    def __init__(self, tarefa):  # Método construtor que recebe a tarefa como parâmetro
        id = random.randint(1000, 9999)  # Gera um número aleatório entre 1000 e 9999 para o ID da tarefa
        self.id = int(id)  # Converte o ID para inteiro
        self.tarefa = tarefa  # Atribui a tarefa passada como parâmetro para a instância atual
        self.tarefa = f"{self.id} - {self.tarefa}"  # Formata a tarefa com o ID e o texto da tarefa

        if DAO.AdicionarTarefa(self.tarefa) == True:  # Se a tarefa foi adicionada com sucesso
            print("Tarefa Adicionada")  # Imprime uma mensagem de sucesso
        else:  # Se a tarefa não foi adicionada com sucesso
            print("Não foi possível adicionar a tarefa. Verifique o índice.")  # Imprime uma mensagem de erro

class ControllerExcluirTarefa:  # Define a classe ControllerExcluirTarefa
    def __init__(self, excluir):  # Método construtor que recebe o índice da tarefa a ser excluída como parâmetro
        self.excluir = excluir  # Atribui o índice passado como parâmetro para a instância atual
        self.excluir = int(excluir) - 1  # Converte o índice para inteiro e subtrai 1 para obter o índice correto na lista

        if self.excluir >= 0 and self.excluir < len(DAO.listarTarefas()):  # Se o índice é válido (está dentro do intervalo da lista)
            tarefa = DAO.listarTarefas()[self.excluir]  # Obtém a tarefa correspondente ao índice
            tarefa_parts = tarefa.split(" - ", 1)  # Divide a tarefa em duas partes: ID e texto da tarefa

            if len(tarefa_parts) > 1:  # Se a tarefa foi dividida corretamente em duas partes
                _, texto_tarefa = tarefa_parts  # Ignora o ID e obtém apenas o texto da tarefa
                print(f"Excluindo a tarefa: {texto_tarefa}")  # Imprime uma mensagem informando qual tarefa está sendo excluída
                if DAO.ExcluirTarefa(self.excluir):  # Se a tarefa foi excluída com sucesso
                    print("Tarefa Excluída")  # Imprime uma mensagem de sucesso
                else:  # Se a tarefa não foi excluída com sucesso
                    print("Não foi possível excluir a tarefa. Verifique o índice.")  # Imprime uma mensagem de erro
            else:  # Se a tarefa não foi dividida corretamente em duas partes
                print("Tarefa não encontrada.")  # Imprime uma mensagem de erro
        else:  # Se o índice é inválido (está fora do intervalo da lista)
            print("Índice inválido.")  # Imprime uma mensagem de erro

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
