from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Cria o motor do banco de dados, é o conecta com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão de banco de dados, é quem vai executar as queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db # Yield no lugar do return para poder chamar varias vezes, return faz apenas 1x
    finally:
        db.close()