# API de Blog Simples

Esta é uma API simples para um blog, onde você pode criar, ler e apagar posts, bem como criar, ler e apagar usuários.

## Endpoints

### Posts

- `GET /posts`: Obter todos os posts.
- `POST /posts`: Criar um novo post.
- `GET /posts/{post_id}`: Obter um post específico por ID.
- `DELETE /posts/{post_id}`: Apagar um post por ID.

### Usuários

- `GET /users`: Obter todos os usuários.
- `POST /users`: Criar um novo usuário.
- `GET /users/{user_id}`: Obter um usuário específico por ID.
- `DELETE /users/{user_id}`: Apagar um usuário por ID.

## Requisitos

- Python 3.x
- FastAPI
- SQLAlchemy
- Banco de dados (por exemplo, SQLite, PostgreSQL, etc.)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/charlesbrito/API_BLOG.git


# Crie e ative um ambiente virtual (opcional, mas recomendado):

## Windows
  ```bash
  python3 -m venv venv
```
  ```bash
  venv\Scripts\activate
```
## MacOS e Linux
  ```bash
python3 -m venv venv
```
  ```bash
source venv/bin/activate
```

# Instale as dependências:
  ```bash
pip install -r requirements.txt
```

# Configuração do Banco de Dados:
- Edite o arquivo database.py para configurar o URL do seu banco de dados.
- Modifique o arquivo models.py conforme necessário para definir as tabelas do banco de dados.

# Execute o aplicativo:
  ```bash
uvicorn main:app --reload
```

# Uso:
- Para obter todos os posts, faça uma solicitação GET para http://localhost:8000/posts.

- Para criar um novo post, faça uma solicitação POST para http://localhost:8000/posts com os dados do post no corpo da solicitação.

- Para obter um post específico por ID, faça uma solicitação GET para http://localhost:8000/posts/{post_id}.

- Para apagar um post por ID, faça uma solicitação DELETE para http://localhost:8000/posts/{post_id}.

- Para obter todos os usuários, faça uma solicitação GET para http://localhost:8000/users.

- Para criar um novo usuário, faça uma solicitação POST para http://localhost:8000/users com os dados do usuário no corpo da solicitação.

- Para obter um usuário específico por ID, faça uma solicitação GET para http://localhost:8000/users/{user_id}.

- Para apagar um usuário por ID, faça uma solicitação DELETE para http://localhost:8000/users/{user_id}.

# Exemplos de Solicitação (com cURL):
- Obter todos os posts:
  ```bash
  http://localhost:8000/posts
  ```
- Criar um novo post:
  ```bash
  -X POST http://localhost:8000/posts -H "Content-Type: application/json" -d '{"title": "Novo Post", "content": "Conteúdo do novo post", "user_id": 1}'
  ```
- Obter um post por ID:
  ```bash
  http://localhost:8000/posts/1
  ```
- Apagar um post por ID:

```bash
curl -X DELETE http://localhost:8000/posts/1
```
- Obter todos os usuários:

```bash
curl http://localhost:8000/users
```
-Criar um novo usuário:
```bash
curl -X POST http://localhost:8000/users -H "Content-Type: application/json" -d '{"username": "novousuario"}'
```
- Obter um usuário por ID:

```bash
curl http://localhost:8000/users/1
```
- Apagar um usuário por ID:

```bash
curl -X DELETE http://localhost:8000/users/1
```

# Observações
- Certifique-se de fornecer os dados corretos no corpo das solicitações POST para criar novos posts e usuários.
- Este é um exemplo simples de uso e não inclui autenticação ou validação de entrada. Certifique-se de implementar esses recursos para sua própria aplicação.
- Para mais detalhes sobre como usar a API, consulte a documentação interativa em http://localhost:8000/docs

