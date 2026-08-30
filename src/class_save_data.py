import json


class SaveData:
    @staticmethod
    def save_json(data):
        with open(f'../data/planes_json.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file)

    @staticmethod
    def save_csv(data):
        with open(f'../data/planes_json.json', 'w', encoding='UTF-8', newline='') as file:
            pass

    @staticmethod
    def save_txt(data):
        with open(f'../data/planes_json.json', 'w', encoding='UTF-8', newline='') as file:
            pass

    @staticmethod
    def save_excel(data):
        with open(f'../data/planes_json.json', 'w', encoding='UTF-8', newline='') as file:
            pass



date = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


if __name__ == '__main__':

    SaveData.save_json(date)