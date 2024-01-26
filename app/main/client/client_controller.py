from flask_restx import Resource, Namespace, fields
from flask import request
from app.main.client.client_db import clientDb

api = Namespace('client', description='Manutençaõ dado do cliente')
#Criação do modelo que será validado ao receber post
modelo = api.model('ClientModel', {
    'id': fields.Integer,
    'nome': fields.String,
    'endereco': fields.String
})

@api.route('/')
class ClientController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return clientDb.obter(), 200
    @api.expect(modelo)
    def post(self):
        return clientDb.adicionar(request.json), 201
    
@api.route('/<int:id>')
class ClientControllerById(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int):
        return clientDb.obter(int(id)), 200
    
    @api.response(200, "Busca realizada com sucesso")
    @api.param('nome', 'Nome do cliente')
    @api.param('endereco', 'Endereço da pessoa')
    def put(self, id:int):
        return clientDb.alterar(int(id), request.json), 201
    
    def delete(self, id:int):
        return clientDb.remover(int(id)), 200