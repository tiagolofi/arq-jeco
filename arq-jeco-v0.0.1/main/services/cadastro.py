
from main.logs import Logger
from main.models import Usuario
from main.database import MemoryDB

class Cadastro():
    def __init__(self, email: str, password: str, nome: str, headers: dict):
        self.USER = Usuario(email, password, nome, headers) # Email() é um objeto
        self.db = MemoryDB()

    def salvarCadastro(self):
        Logger.log(Logger.INFO, 'Persitindo %s no banco de dados...', self.USER().get('email'))
        self.db.save(
            self.USER()
        )

    def retornaCadastro(self):
        return self.db.read()
