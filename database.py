# Essas são todas as importações necessárias para a conexão com Banco de Dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de conexão com o banco de dados, por favor, insira dentro das aspas a URL de conexão com seu Bando de dados ! VLW
URL_DATABASE = ""

# Criação da engine
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()