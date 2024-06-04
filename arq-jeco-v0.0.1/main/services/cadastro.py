
from main.logs import Logger
from main.models import Email
from main.database import MemoryDB

class Cadastro():
    def __init__(self, email: str, password: str):
        self.email = email
        self.dados = Email(self.email, password)
        self.db = MemoryDB()

    def salvarCadastro(self):
        Logger.log(Logger.INFO, 'Persitindo %s no banco de dados...', self.email)
        self.db.save(
            self.dados()
        )

    def retornaCadastro(self):
        return self.db.read()
