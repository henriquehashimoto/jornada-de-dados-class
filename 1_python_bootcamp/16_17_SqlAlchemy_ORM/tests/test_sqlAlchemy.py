from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String



#--------------------------
# Creating a database
#--------------------------
engine = create_engine("sqlite:///alchemyDB.db", echo=True)


#--------------------------
# Creating the table
#--------------------------
# Criando um objetivo que irá informar que uma tabela será criada
base = declarative_base()

class Usuario(base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Cria a tabela no banco
base.metadata.create_all(engine)


#--------------------------
# Inserting data
#--------------------------
session_maker = sessionmaker(bind=engine)
session = session_maker()

# Objects with the values to be added
novo_usuario = Usuario(nome="Henrique", idade=29)
# novo_user2 = Usuario(id=2,nome="Keth", idade=29)

# Inserting data 
session.add(novo_usuario)
# session.add(novo_user2)

# Commit inserts
session.commit()


#--------------------------
# Consulting data
#--------------------------
select_userss = session.query(Usuario).filter_by(nome="Henrique").first()
print(select_userss.nome, select_userss.idade)

