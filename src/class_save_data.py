import json


class SaveData:
    @staticmethod
    def save_json(data):
        with open('../data/planes_json.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file)

    @staticmethod
    def save_csv(data):
        with open('../data/planes_json.json', 'w', encoding='UTF-8', newline=''):
            pass

    @staticmethod
    def save_txt(data):
        with open('../data/planes_json.json', 'w', encoding='UTF-8', newline=''):
            pass

    @staticmethod
    def save_excel(data):
        with open('../data/planes_json.json', 'w', encoding='UTF-8', newline=''):
            pass
