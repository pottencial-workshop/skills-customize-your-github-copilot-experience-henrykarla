# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Nesta tarefa, você aprenderá a construir uma API REST completa usando o framework FastAPI do Python. Você criará uma API para gerenciar uma lista de tarefas (To-Do List) com operações CRUD (Create, Read, Update, Delete), validação de dados e documentação automática.

## 📝 Tarefas

### 🛠️ Tarefa 1: Configurar o Ambiente FastAPI

#### Description
Configure seu ambiente de desenvolvimento instalando o FastAPI e suas dependências. Crie a estrutura básica da aplicação com um endpoint de teste.

#### Requirements
Seu projeto deve:

- Instalar FastAPI e Uvicorn (servidor ASGI)
- Criar um arquivo `main.py` com a aplicação FastAPI
- Implementar um endpoint GET `/` que retorna uma mensagem de boas-vindas
- Executar o servidor e acessar a documentação automática em `/docs`


### 🛠️ Tarefa 2: Implementar o Modelo de Dados

#### Description
Crie modelos de dados usando Pydantic para validar as requisições da API. Defina a estrutura de uma tarefa (Task) com seus campos e validações.

#### Requirements
O modelo deve incluir:

- Campo `id` (inteiro) - identificador único da tarefa
- Campo `title` (string) - título da tarefa (obrigatório, mínimo 3 caracteres)
- Campo `description` (string) - descrição detalhada (opcional)
- Campo `completed` (boolean) - status de conclusão (padrão: False)
- Campo `created_at` (datetime) - data de criação


### 🛠️ Tarefa 3: Criar Endpoints CRUD

#### Description
Implemente os endpoints para realizar operações CRUD completas na API de tarefas.

#### Requirements
A API deve ter os seguintes endpoints:

- `GET /tasks` - Listar todas as tarefas
- `GET /tasks/{id}` - Obter uma tarefa específica por ID
- `POST /tasks` - Criar uma nova tarefa
- `PUT /tasks/{id}` - Atualizar uma tarefa existente
- `DELETE /tasks/{id}` - Deletar uma tarefa
- Retornar códigos de status HTTP apropriados (200, 201, 404, etc.)
- Implementar tratamento de erros (tarefa não encontrada, etc.)


### 🛠️ Tarefa 4: Testar a API

#### Description
Teste todos os endpoints da sua API usando a documentação interativa do FastAPI (Swagger UI) ou ferramentas como Postman/curl.

#### Requirements
Você deve testar:

- Criar pelo menos 3 tarefas diferentes
- Listar todas as tarefas criadas
- Obter uma tarefa específica por ID
- Atualizar o status de uma tarefa para "completed"
- Deletar uma tarefa
- Verificar tratamento de erros (tentar obter uma tarefa com ID inexistente)
- Documentar os resultados dos testes (screenshots ou descrição)


## 📚 Resources

- [Documentação Oficial do FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## 🎓 Learning Goals

Ao completar esta tarefa, você será capaz de:

- Configurar e estruturar uma aplicação FastAPI
- Criar modelos de dados com validação usando Pydantic
- Implementar endpoints REST com operações CRUD
- Utilizar diferentes métodos HTTP (GET, POST, PUT, DELETE)
- Trabalhar com códigos de status HTTP apropriados
- Usar a documentação automática do FastAPI para testar APIs

## 💡 Tips

- Use a documentação interativa em `/docs` para testar seus endpoints em tempo real
- Comece simples e adicione funcionalidades gradualmente
- Preste atenção aos códigos de status HTTP - eles comunicam o resultado da operação
- Use type hints do Python - o FastAPI utiliza-os para validação automática
- Para armazenar as tarefas, você pode usar uma lista em memória inicialmente (não precisa de banco de dados nesta tarefa)

## 🚀 Bonus Challenges (Optional)

Se você terminar antes e quiser desafios extras:

- Adicionar filtros à listagem de tarefas (ex: listar apenas tarefas completadas)
- Implementar paginação na listagem de tarefas
- Adicionar um campo de prioridade às tarefas (baixa, média, alta)
- Criar um endpoint para estatísticas (total de tarefas, completadas, pendentes)
- Adicionar validação customizada (ex: data de vencimento não pode ser no passado)
