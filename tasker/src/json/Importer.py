import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open('taski.json', encoding='UTF-8') as json_file:
            data = json.load(json_file)
            return data

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.read_tasks()