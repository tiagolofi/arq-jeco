
from flask import Flask, jsonify, request
from dotenv import load_dotenv

from main.services import Cadastro

load_dotenv()
app = Flask(__name__)

app.route('/register', methods = ['POST'])
def register():
    cadastro = Cadastro(request.form['email'], request.form['password'])
    cadastro.salvarCadastro()
    return jsonify(
        {'msg': 'Deu certo'}
    )

if __name__ == '__main__':
    app.run(debug = True)
