
class ErrorSave(Exception):
    def __init__(self, message = "Não foi possível persistir os dados", errors = None):
        super().__init__(message)
        self.errors = errors