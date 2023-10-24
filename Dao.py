
class Dao:  # Define a classe Dao
    def __init__ (self):  # Método construtor sem parâmetros
        self.arquivo  = "tarefas.txt"  # Define o nome do arquivo onde as tarefas serão armazenadas
        with open (self.arquivo, "a") as arquivo:
            arquivo.write("ID --- Tarefa \n")
            arquivo.close()

    def AdicionarTarefa(self, tarefa):  # Define o método AdicionarTarefa que recebe a tarefa como parâmetro
        try:  # Tenta executar o bloco de código dentro do try

            with open(self.arquivo, "a") as arquivo:  # Abre o arquivo em modo de anexação ("a")
                arquivo.write(tarefa + "\n") # Escreve a tarefa no arquivo seguida de uma quebra de linha
                #O Arquivo ter como padrão ja escrito ID - Tarefa
                
                return True  # Retorna True indicando que a tarefa foi adicionada com sucesso

        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__)  # Imprime o nome da classe do erro
            return False  # Retorna False indicando que a tarefa não foi adicionada com sucesso
        
    def listarTarefas(self):  # Define o método listarTarefas que não recebe nenhum parâmetro
        try:  # Tenta executar o bloco de código dentro do try
            with open(self.arquivo, "r") as arquivo:  # Abre o arquivo em modo de leitura ("r")
                return arquivo.readlines()  # Retorna uma lista contendo todas as linhas do arquivo

        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__)  # Imprime o nome da classe do erro
            return False  # Retorna False indicando que as tarefas não foram listadas com sucesso

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

                if DAO.ExcluirTarefa(self.excluir - 1):
                    print("Tarefa Excluída")
                else:
                    print("Não foi possível excluir a tarefa. Verifique o índice.")
            else:
                print("Tarefa não encontrada.")
        else:
            print("Índice inválido.")



DAO = Dao()  # Cria uma instância da classe Dao e atribui à variável DAO
