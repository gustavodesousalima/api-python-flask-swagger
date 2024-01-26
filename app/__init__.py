from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Aplica o middleware ProxyFix para corrigir o problema com o endereço IP incorreto sendo detectado ao executar atrás de um proxy
app.wsgi_app = ProxyFix(app.wsgi_app)

# Cria um Blueprint para a API
blueprint = Blueprint('api', __name__)

# Registra o Blueprint com o aplicativo Flask
app.register_blueprint(blueprint)

# Criar uma instância da API Flask-RestPlus
api = Api(app, title='Api Flask', version='1.0', description='Api construída utilizando Python, Flask e Swagger', prefix='/api')