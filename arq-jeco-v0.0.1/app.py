
from flask import Flask, jsonify, request
# from dotenv import load_dotenv

from main.services import Cadastro
from main.services import Desafio

# load_dotenv()
app = Flask(__name__)

@app.route('/register', methods = ['POST'])
def register():
    cadastro = Cadastro(request.form['email'], request.form['password'], request.form['nome'], dict(request.headers))
    cadastro.salvarCadastro()
    return jsonify(
        cadastro.retornaCadastro()
    )

@app.route('/login', methods = ['POST'])
def login():
    desafio = Desafio(request.form['email'], request.form['password'], dict(request.headers))
    desafio.salvarDesafio()
    return jsonify(
        desafio.retornaDesafio()
    )

if __name__ == '__main__':
    app.run(debug = True)
