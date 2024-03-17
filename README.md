# Flask com MongoDB via Docker

Este é um projeto básico demonstrando como configurar um aplicativo Flask com MongoDB utilizando Docker para desenvolvimento.

# Tema: Aplicativo de Lista de Compras (API)

Nosso aplicativo de Lista de Compras permitirá que os usuários criem e gerenciem suas listas de compras. Os principais recursos incluirão:

Criação de Lista de Compras: Os usuários podem criar novas listas de compras.

Adição de Itens à Lista: Os usuários podem adicionar itens à lista de compras, incluindo nome do item, quantidade e opcionalmente a categoria.

Visualização de Lista de Compras: Os usuários podem visualizar suas listas de compras, incluindo todos os itens adicionados.

Atualização de Itens na Lista: Os usuários podem marcar itens como comprados, atualizar a quantidade de itens ou remover itens da lista.

Exclusão de Lista de Compras: Os usuários podem excluir listas de compras que não são mais necessárias.

## Requisitos

- Docker
- Docker Compose

## Instalação

1. Clone este repositório:

`git clone https://github.com/pedro-demeu/flask-mongodb.git`

2. Navegue até o diretório do projeto:

`cd flask-mongo-docker`

3. Execute o comando docker-compose para iniciar o projeto:

`docker-compose up --build`

## Uso

- O aplicativo Flask estará disponível em http://localhost:5000
- O MongoDB estará disponível na porta padrão 27017

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
