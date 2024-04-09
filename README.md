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

## Crie e ative um ambiente virtual (opcional, mas recomendado):


```bash 
python3 -m venv venv```

source venv/bin/activate

## Instale as dependências:

  
pip install -r requirements.txt

## Configuração do Banco de Dados
Edite o arquivo database.py no diretório ./app para configurar o URL do seu banco de dados.
Modifique o arquivo models.py no diretório ./app conforme necessário para definir as tabelas do banco de dados.

## Execute o aplicativo:
 
uvicorn main:app --reload

## Uso
Para obter todos os posts, faça uma solicitação GET para http://localhost:8000/posts.

Para criar um novo post, faça uma solicitação POST para http://localhost:8000/posts com os dados do post no corpo da solicitação.

Para obter um post específico por ID, faça uma solicitação GET para http://localhost:8000/posts/{post_id}.

Para apagar um post por ID, faça uma solicitação DELETE para http://localhost:8000/posts/{post_id}.

Para obter todos os usuários, faça uma solicitação GET para http://localhost:8000/users.

Para criar um novo usuário, faça uma solicitação POST para http://localhost:8000/users com os dados do usuário no corpo da solicitação.

Para obter um usuário específico por ID, faça uma solicitação GET para http://localhost:8000/users/{user_id}.

Para apagar um usuário por ID, faça uma solicitação DELETE para http://localhost:8000/users/{user_id}







