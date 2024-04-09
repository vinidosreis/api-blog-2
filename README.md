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
   git clone https://github.com/seu_usuario/sua_api_blog.git

## Crie e ative um ambiente virtual (opcional, mas recomendado):
python3 -m venv venv
source venv/bin/activate

## Instale as dependências:
pip install -r requirements.txt

## Execute o aplicativo:
uvicorn main:app --reload





