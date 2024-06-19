
from random import sample
from hashlib import sha256
from main.logs import Logger

ALFNUM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

class Hash:

    TOKEN_L4 = ''.join(sample(ALFNUM, 4))
    TOKEN_L8 = ''.join(sample(ALFNUM, 8))
    TOKEN_L12 = ''.join(sample(ALFNUM, 12))
    SALT = ''.join(sample(ALFNUM, 7))

    def encrypt(texto):
        Logger.log(Logger.INFO, 'Encriptando credenciais')
        return sha256(texto.encode()).hexdigest()
