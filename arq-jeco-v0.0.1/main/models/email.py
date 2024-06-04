
import os
from hashlib import sha256

from main.logs import Logger
from main.hashing import Hash
from main.utils import DateLocal

class Email():
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        self.salt = os.environ['SALT']
        self.token = Hash.TOKEN_L12
        self.datahora = DateLocal.BR_STR

    def encrypt(self):
        Logger.log(Logger.INFO, 'Encriptando senha: %s', self.email)
        return sha256(f'''{self.email}{self.password}{self.salt}'''.encode()).hexdigest()

    def __call__(self) -> dict:
        Logger.log(Logger.INFO, 'Email: %s', self.email)
        return {
            'token_id': self.token,
            'email': self.email,
            'datahora': self.datahora,
            'credentials': self.encrypt()
        }
