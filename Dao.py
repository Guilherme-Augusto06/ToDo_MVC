class Dao:  # Define a classe Dao
    def __init__ (self):  # Método construtor sem parâmetros
        self.arquivo  = "tarefas.txt"  # Define o nome do arquivo onde as tarefas serão armazenadas

    def AdicionarTarefa(self, tarefa):  # Define o método AdicionarTarefa que recebe a tarefa como parâmetro
        try:  # Tenta executar o bloco de código dentro do try
            with open(self.arquivo, "a") as arquivo:  # Abre o arquivo em modo de anexação ("a")
                arquivo.write(tarefa + "\n")  # Escreve a tarefa no arquivo seguida de uma quebra de linha
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

    def ExcluirTarefa(self):  # Define o método ExcluirTarefa que não recebe nenhum parâmetro
        try:  # Tenta executar o bloco de código dentro do try
            with open(self.arquivo, "w") as arquivo:  # Abre o arquivo em modo de escrita ("w")
                return arquivo.write("")  # Escreve uma string vazia no arquivo, efetivamente apagando todo o seu conteúdo

        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__)  # Imprime o nome da classe do erro
            return False  # Retorna False indicando que a tarefa não foi excluída com sucesso

DAO = Dao()  # Cria uma instância da classe Dao e atribui à variável DAO
