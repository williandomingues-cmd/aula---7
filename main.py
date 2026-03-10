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
class Produto(Base):

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

    ativo = Column(Boolean)

    #metodo construtor 
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

    #representacao do objeto para imprimir
    def __repr__(self):
        return f"Produto(id={self.id}, nome={self.nome}, preco={self.preco}, estoque{self.estoque}, ativo{self.ativo} )"
    
#criar a conexão com sqlite
engine = create_engine("sqlite:///estoque.db", echo=True)

#criar as tabelas no banco se ainda nao existirem
Base.metadata.create_all(engine)


#criar uma fabrica de sessões conectadas ao banco 
Session = sessionmaker(bind=engine)

session = Session()

# criar objeto Produtos
produto1 = Produto("Notebook", 5500, 6, True)
produto2 = Produto("Teclado", 500, 100, True)
produto3 = Produto("Mouse", 150, 55, True)

# Adicionar os produtos na sessão (carrinho)
session.add(produto1)
session.add(produto2)
session.add(produto3)

# Confirmar a inserção no banco
# Salvar no banco de dados
session.commit()

# Listar
# Buscar todos os produtos do banco
Produtos = session.query(Produto).all()

print(Produtos)

for p in Produtos:
    print(f"id={p.id}, nome={p.nome}, preco={p.preco}, estoque={p.estoque}, ativo={p.ativo}")

# UPDATE (atualizar)

#Buscar o produto com id = 1
produto_id = session.query(Produto).filter(Produto.id == 1).first()
# print(produto_id)

produto_estoque = session.query(Produto).filter(Produto.estoque >= 10).all()
# for produto in produto_estoque:
#     print(produto.estoque)

produto_id2 = session.query(Produto).filter_by(id=1).first()
# print(produto_id2)

# Podemos usar order by
produtos_organizados = session.query(Produto).order_by(Produto.estoque).all()
produtos_organizados2 = session.query(Produto).order_by(Produto.estoque.desc()).all()
# for produto in produtos_organizados:
#     print(f"Nome: {produto.nome}, Qtd_estoque: {produto.estoque}")

#Limitar a quantidade de resultado - tops produtos mais
produtos_mais_caros = session.query(Produto).order_by(Produto.estoque).limit(5).all()
for produto in produtos_mais_caros:
    print(f"Nome: {produto.nome}, Valor: {produto.preco}")

# Update - Atualizar
#Busquei o produto para atualizar
notebook = session.query(Produto).filter_by(id=1).first()
notebook.preco = 6000

#Confirmar essa alteração
session.commit()
print("Preço atualizado com sucesso")

produtos = session.query(Produto).all()

for p in produtos:
    print(f"id={p.id}, nome={p.nome}, preco={p.preco}, estoque={p.estoque}, ativo={p.ativo}")