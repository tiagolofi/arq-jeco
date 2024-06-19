
from main.logs import Logger
from main.hashing import Hash
from main.utils import DateLocal

class Usuario():
    def __init__(self, email: str, password: str, nome: str, headers: dict) -> None:
        self.email = email
        self.nome = nome
        self.password = password
        self.salt = Hash.SALT
        self.token = Hash.TOKEN_L12
        self.datahora = DateLocal.BR_STR
        self.headers = headers
        self.credencial = Hash.encrypt(f'''{self.email}{self.password}{self.salt}''')

    def __call__(self) -> dict:
        Logger.log(Logger.INFO, 'Usuário: %s', self.email)
        return {
            'token_id': self.token,
            'email': self.email,
            'nome': self.nome,
            'datahora': self.datahora,
            'salt': self.salt,
            'credencial': self.credencial,
            'headers': self.headers
        }
