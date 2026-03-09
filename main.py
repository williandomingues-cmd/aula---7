# Importa a função responsável por criar a conexão com o banco
from sqlalchemy import create_engine

# Importa tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importa a classe Base usada para criar os modelos orm
from sqlalchemy.orm import declarative_base

# Importa ferramenta para criar sessões de banco
from sqlalchemy.orm import sessionmaker

#Criar classe base do ORM
Base = declarative_base()

# cl¡sses = Tabelas
# Objeto = Linha tabela
# Atributos = Coluna

#classe produto represetando uma tabela no banco de dados 
class produto(Base):

    __tablename__ = "produtos"

    #coluna id 
    # integer > numero inteiro 
    # primary_key = true 
    id = Column(Integer, primary_key=True)

    #nome do produto 
    # String > texto
    nome = Column(String(100))

    #preço do produto 
    #float : numero decimal 
    preco = Column(Float)

#qualidade em estoque
estoque = Column(Float)


#metodo construtor 
def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

#representacao do objeto para imprimir
def __repr__(self):
        return f"produto(id={self.id}, nome={self.nome}, preco={self.preco}, estoque{self.estoque}, ativo{self.ativo} )"
    
#criar a conexão com sqlite
engine = create_engine("sqlite:///estoque.db", echo=True)

#criar as tabelas no banco se ainda nao existirem
Base.metadata.create_all(engine)

