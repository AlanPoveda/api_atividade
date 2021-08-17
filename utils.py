from models import Pessoas, db_session

#Create na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Ruffo', idade=22)
    print(pessoa)
    pessoa.save()

#Listar pessoas da tabel
def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)

#Consulta somente uma pessoa da tabela pessoa
def consultaByName():
    pessoa = Pessoas.query.filter_by(nome='Alan').first()
    print(pessoa.idade)

#Altera dados da table pessoa
def updatePessoa():
    pessoa = Pessoas.query.filter_by(nome='Alan').first()
    pessoa.idade = 21
    pessoa.save()

#delete pessoa da tabela
def deletePessoa():
    pessoa = Pessoas.query.filter_by(nome='Ruffo').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    updatePessoa()
    #consultaByName()
    #deletePessoa()
    consulta()
