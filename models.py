from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship #resposavel pela secção, consultas
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
#Aqui ele abre o banco e faz a seção
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
#Criar o banco de dados com SQLITE, fazer as alterações
Base = declarative_base()
Base.query = db_session.query_property()

#Criando a tabela
class Pessoas(Base):
    __tablename__='pessoas' #nome da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True) #Esse index é para para procurar mais fácil
    idade = Column(Integer)

    #Impresão da consulta, somente o nome
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    #Salva e commita no banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    #Deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()


#Tabela atividades

class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    #ForeingKey  tabela pessoas
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")
    #---------------------------------

    # Impresão da consulta da tabela
    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    # Salva e commita no banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Deletar
    def delete(self):
        db_session.delete(self)
        db_session.commit()

#Aqui ele cria o banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()