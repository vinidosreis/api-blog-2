# Essas são todas as importações necessárias para a criação de tabelas no BD
from sqlalchemy import Boolean, Column, Integer, String
from database import base

# Criação da tabela usuários
class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)


# Criação da tabela post
class Post(base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer)