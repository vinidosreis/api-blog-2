# Essas são todas as importações necessárias para a criação da API
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

# Criando API
app = FastAPI()
models.base.metadata.create_all(bind=engine)

# Classes para definir atributos das nossas tabelas
class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

# Para pegar nosso banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

# Endpoint para criar post
@app.post("/posts/", tags = ["post"], status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db:db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()


# Endpoint para ler post por ID
@app.get("/posts/{post_id}", tags = ["post"], status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db:db_dependency):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail='Post não encontrado')
    return post

# Endpoit para listar todos os posts
@app.get("/posts/", tags = ["post"], status_code=status.HTTP_200_OK)
async def read_all_posts(db: db_dependency):
    post = db.query(models.Post).all()
    return post


# Endpoit para deletar post
@app.delete("/posts/{post_id}", tags = ["post"], status_code=status.HTTP_200_OK)
async def delete_post(post_id:int, db:db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post não encontrado')
    db.delete(db_post) 
    db.commit()

# Endpoit para criar usuário
@app.post("/users/", tags = ["user"], status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()

# Endpoint para ler usuário por id 
@app.get("/users/{user_id}", tags = ["user"], status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db:db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return user

# Endpoint para ler todos os usuários
@app.get("/users/", tags = ["user"], status_code=status.HTTP_200_OK)
async def read_all_users(db:db_dependency):
    user = db.query(models.User).all()
    return user


# Endpoit para deletar usuário por id 
@app.delete("/users/{user_id}", tags = ["user"], status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db:db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    db.delete(db_user)
    db.commit()





