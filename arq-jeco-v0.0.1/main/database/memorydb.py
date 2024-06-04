
from main.logs import Logger
from main.exceptions import ErrorSave

class MemoryDB():
    def __init__(self):
        self.db = []

    def save(self, data: dict):
        try:
            self.db.append(data)
            Logger.log(Logger.INFO, 'Dados gravados com sucesso!')
        except Exception as e:
            Logger.log(Logger.ERROR, e)
            ErrorSave(errors = e)

    def read(self):
        return self.db
