import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        with open('taski.json', 'w', encoding='UTF-8') as json_file:
            json.dump(tasks, json_file, indent=4, ensure_ascii=False)


