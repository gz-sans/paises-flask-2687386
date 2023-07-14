from flask import Flask

#crear un objeto flask
#_name almacena donde quiera que se invoque el modulo que se va a almacenar 
app = Flask(__name__)

#crea una ruta

@app.route('/')
def index():
    return 'hola 2687386'