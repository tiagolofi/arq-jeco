
import json
from main.logs import Logger
from main.exceptions import ErrorSave
import os

class MemoryDB():
    def __init__(self):
        with open('db.json', 'r') as file:
            self.db = json.load(file)

    def save(self, data: dict):
        try:
            self.db.append(data)
            with open('db.json', 'w') as file:                                                    
                json.dump(self.db, file, indent = 2)
            Logger.log(Logger.INFO, 'Dados gravados com sucesso!')
        except Exception as e:
            Logger.log(Logger.ERROR, e)
            ErrorSave(errors = e)

    def read(self):
        return self.db
