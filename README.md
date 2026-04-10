# Users CRUD API com FastAPI, MongoDB e Docker

Uma API RESTful completa para gerenciamento de usuários desenvolvida com **FastAPI**, utilizando **MongoDB** como banco de dados e **Docker** para containerização.

## 🚀 Tecnologias

- **FastAPI**: Framework web moderno e rápido para APIs Python
- **MongoDB**: Banco de dados NoSQL
- **Docker & Docker Compose**: Containerização
- **Uvicorn**: Servidor ASGI
- **Pydantic**: Validação de dados

## 📋 Pré-requisitos

- Docker
- Docker Compose

## 🔧 Instalação Rápida

1. Clone o repositório:
```bash
git clone https://github.com/Jeanlukas1/users-crud-fastapi-docker-mongodb.git
cd users-crud-fastapi-docker-mongodb
```

2. Inicie os containers:
```bash
docker-compose up -d
```

Pronto! A aplicação estará rodando em `http://localhost:8000`

## 📖 Documentação Interativa

Acesse a documentação da API em:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔌 Endpoints da API

### Base URL
```
http://localhost:8000
```

### Usuários

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| **GET** | `/` | Health check |
| **GET** | `/users` | Lista todos os usuários |
| **POST** | `/users` | Cria um novo usuário |
| **GET** | `/users/{id}` | Obtém um usuário específico |
| **PUT** | `/users/{user_id}` | Atualiza um usuário |
| **DELETE** | `/users/{user_id}` | Deleta um usuário |

### Exemplo de Requisição

#### Criar um usuário (POST)
```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "email": "joao@example.com",
    "idade": 30
  }'
```

**Resposta:**
```json
{
  "message": "User Created",
  "id": "507f1f77bcf86cd799439011"
}
```

#### Listar usuários (GET)
```bash
curl "http://localhost:8000/users"
```

**Resposta:**
```json
[
  {
    "_id": "507f1f77bcf86cd799439011",
    "nome": "João Silva",
    "email": "joao@example.com",
    "idade": 30
  }
]
```

## 📦 Estrutura do Projeto

```
.
├── main.py                          # Aplicação FastAPI
├── requirements.txt                 # Dependências Python
├── README.md                        # Este arquivo
├── docs/
│   └── End-Points.postman_collection.json  # Coleção Postman
└── src/
    ├── __init__.py
    ├── db/
    │   ├── __init__.py
    │   └── database.py             # Configuração MongoDB
    ├── docker/
    │   └── docker-compose.yml      # Orquestração containers
    ├── routes/
    │   ├── __init__.py
    │   └── user_routes.py          # Rotas da API
    └── schema/
        ├── __init__.py
        └── user_schema.py          # Schema Pydantic
```

## 🐳 Docker Compose

### Serviços

- **FastAPI**: Aplicação principal na porta 8000
- **MongoDB**: Banco de dados na porta 27018

### Comando Docker

Subir os containers (detached):
```bash
docker-compose up -d
```

Parar os containers:
```bash
docker-compose down
```

Ver logs:
```bash
docker-compose logs -f
```

Reconstruir containers:
```bash
docker-compose build
```

## 📊 Modelo de Dados

### User
```json
{
  "_id": "ObjectId",
  "nome": "string",
  "email": "string",
  "idade": "integer"
}
```

## 📝 Schema Pydantic

```python
class User(BaseModel):
    nome: str
    email: str
    idade: int
```

## 🔌 Conexão MongoDB

- **URL**: `mongodb://localhost:27018`
- **Database**: `aula_backend`
- **Collection**: `users`

## 🛠️ Desenvolvimento

### Instalação Local (sem Docker)

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
uvicorn main:app --reload
```

## 📄 Postman

Acesse o link `https://www.postman.com/lukasjean745-1800510/workspace/lista-de-usurios-fastapi-docker-mongodb` do Postman para testar todos os endpoints.

## 📝 Dependências

- fastapi
- uvicorn
- pymongo
- python-dotenv

## 📄 Licença

Este projeto está open source e disponível para uso livre.

## 👨‍💻 Autor

Desenvolvido por Jeanlukas
