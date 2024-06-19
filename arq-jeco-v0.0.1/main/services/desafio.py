                                   
from main.logs import Logger
from main.hashing import Hash
from main.models import Credencial
from main.database import MemoryDB

class Desafio():
    def __init__(self, email: str, password: str, headers: dict):
        self.email = email
        self.password = password
        self.CRED = Credencial(email, password, headers)
        self.db = MemoryDB()

    def desafio(self) -> str:
        data = self.db.read() # refazer implementação no mongo db
        if data[0].get('email') == self.email: # and i['senha'] == self.password: 
            texto = f'''{self.email}{self.password}{data[0].get('salt')}'''
            if Hash.encrypt(texto) == data[0].get('credencial'):
                Logger.log(Logger.INFO, 'Acesso permitido para %s', self.email)
                self.CRED.setDesafio(True)
            else:
                Logger.log(Logger.ERROR, 'Senha incorreta')
                self.CRED.setDesafio(False)
        else:
            Logger.log(Logger.ERROR, 'Email inválido')
            self.CRED.setDesafio(False)
    
    def salvarDesafio(self):
        Logger.log(Logger.INFO, 'Persitindo %s no banco de dados...', self.CRED().get('email'))
        self.desafio()
        self.db.save(
            self.CRED()
        )

    def retornaDesafio(self):
        return self.db.read()
