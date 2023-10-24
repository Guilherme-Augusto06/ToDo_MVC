# Aplicação de Lista de Tarefas - Padrão MVC

Este é um exemplo simples de uma aplicação de lista de tarefas usando o padrão Model-View-Controller (MVC). O MVC é uma arquitetura de software que divide a aplicação em três componentes principais: Model, View e Controller. Cada componente tem uma função específica na aplicação.

## Padrão MVC

- **Model:** O Model representa a lógica de negócios da aplicação e os dados. Neste projeto, a classe `ToDo` é o Model e é responsável por gerenciar a lista de tarefas, incluindo adicionar, excluir e listar tarefas. Além disso, a classe `Dao` atua como um componente de persistência de dados para interagir com um arquivo de texto para armazenar tarefas.

- **View:** A View é responsável pela apresentação e interface do usuário. Neste projeto, a classe `VIEW` contém o código para exibir um menu de opções para o usuário e receber sua entrada no console.

- **Controller:** O Controller age como um intermediário entre o Model e a View. Ele recebe as entradas do usuário da View, interage com o Model para realizar operações e atualiza a View com os resultados. As classes `ControllerAdicionarTarefa`, `ControllerExcluirTarefa` e `ControllerListarTarefas` controlam a lógica de adicionar, excluir e listar tarefas, respectivamente.

- **DAO (Data Access Object):** O DAO é um componente responsável por acessar e manipular os dados. Neste projeto, a classe `Dao` é responsável por interagir com um arquivo de texto para armazenar e recuperar tarefas.

## Classes

- **ToDo:** Representa o Model da aplicação e é responsável por gerenciar a lista de tarefas.

- **VIEW:** Representa a View da aplicação e é responsável por exibir o menu de opções e receber a entrada do usuário.

- **ControllerAdicionarTarefa:** Um controlador que lida com a adição de tarefas ao Model.

- **ControllerExcluirTarefa:** Um controlador que lida com a exclusão de tarefas com base no índice fornecido pelo usuário.

- **ControllerListarTarefas:** Um controlador que lista todas as tarefas do Model, formatando a exibição para que o ID não seja visível.

- **Dao:** Uma classe que lida com a persistência de dados, como adicionar, listar e excluir tarefas em um arquivo de texto.

## Uso

Para usar a aplicação, basta executar o arquivo da View no console. A partir daí, você pode escolher entre as opções disponíveis para adicionar, listar ou excluir tarefas.

Certifique-se de ter as dependências adequadas instaladas, que podem incluir Python, de acordo com os requisitos do projeto.

## Contribuições

Este projeto é um exemplo simples do padrão MVC em Python e é destinado apenas para fins educacionais. Sinta-se à vontade para usá-lo como ponto de partida para seus próprios projetos ou contribuir com melhorias se desejar.

## Licença

Este projeto é de código aberto e está disponível sob a [Licença MIT](LICENSE).

