
from main.logs import Logger
from main.utils import DateLocal

class Credencial():
    def __init__(self, email: str, password: str, headers: dict):
        self.email = email
        self.password = password
        self.headers = headers
        self.desafio = None
    
    def setDesafio(self, desafio):
        self.desafio = desafio

    def __call__(self):
        Logger.log(Logger.INFO, 'Credenciais para: %s', self.email)
        return {
            'email': self.email,
            'datahora': DateLocal.BR_STR,
            'auth': self.desafio,
            'headers': self.headers
        }
