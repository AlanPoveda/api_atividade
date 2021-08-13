from flask import Flask, request
from flask_restful import Resource, Api

from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    #GetByName
    def get(self, nome):
        #Parecido com o utils
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            #É um objeto, então precisa fazer o tratamento
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError: #É esse tipo de erro, pois é o que reclamou no console
            message = 'person not found'
            response = {'status':'error', 'message':message}
        return response

    #Update
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        #Aqui ele retorna já em formato json
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade':pessoa.idade,
            'id':pessoa.id
        }
        return response

    def delete(self, instance):
        pessoa = Pessoas.query.filter_by(nome=instance).first()
        pessoa.delete()
        message = 'delete person in database'
        response = {'status': 'sucess','message':message}
        return response

class ListPerson(Resource):
    def get(self):
        person = Pessoas.query.all()
        #Lambida, para colocar todos
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade } for i in person]
        return response

class CreatePerson(Resource):
    def post(self):
        data = request.json
        person = Pessoas(nome=data['nome'], idade=data['idade'])
        person.save()
        response = {
            'id':person.id,
            'nome':person.nome,
            'idade':person.idade
        }
        return response

class ListarAtividades(Resource):
    def get(self):
        atividade = Atividades.query.all()
        response = [{'id':i.id ,'pessoa':i.pessoa.nome, 'nome':i.nome} for i in atividade]
        return response

    def post(self):
        data = request.json
        #Assim ele vai achar a pessoa que vai inserir
        pessoa = Pessoas.query.filter_by(nome=data['pessoa']).first()
        atividade = Atividades(nome=data['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response






api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListPerson, '/pessoas')
api.add_resource(CreatePerson, '/pessoa')
api.add_resource(ListarAtividades, '/atividades')

if __name__ == '__main__':
    app.run(debug=True)
