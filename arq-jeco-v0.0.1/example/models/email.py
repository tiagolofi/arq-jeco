
import logging
from utils import *
from example.exceptions.email_exceptions import NotIsEmail, FornecedorNotFound

class Email:

    def __init__(self, email: str):
        self.email = email
        self.validacao_email = validacao_email(email)
        if self.validacao_email:
            self.fornecedor = validacao_fornecedor_email(email)
        else:
            logging.info('verifique se o endereço de email está escrito corretamente: %s', self.email)
            raise NotIsEmail()

    def __str__(self):
        try:
            return f'''{self.email}\nFornecido por: {self.fornecedor}'''
        except Exception as e:
            logging.info('verifique se o endereço de email está escrito corretamente: %s', self.email)
            raise FornecedorNotFound(errors=e)
