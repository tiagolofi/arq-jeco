
class NotIsEmail(Exception):
    def __init__(self, message = "Isto não é um email válido", errors = None):
        super().__init__(message)
        self.errors = errors

class FornecedorNotFound(Exception):
    def __init__(self, message = "Fornecedor não encontrado", errors = None):
        super().__init__(message)
        self.errors = errors
