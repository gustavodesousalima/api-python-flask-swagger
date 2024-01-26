from app import app
from os import environ

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Obtém o valor da variável de ambiente 'SERVER_HOST' ou usa 'localhost' como padrão
    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    
    # Executa a aplicação Flask no host e porta especificados
    # Habilita o modo de depuração se a variável de ambiente 'ENV' não for igual a 'PRODUCTION'
    # Permite a execução de múltiplas threads
    app.run(host=SERVER_HOST, port=5500, debug=(not environ.get('ENV') == 'PRODUCTION'), threaded=True)