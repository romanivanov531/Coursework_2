import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict


class AirplaneStorage(ABC):
    """Абстрактный интерфейс для хранилища данных о самолётах."""
    @abstractmethod
    def add_airplane(self, airplane: Dict[str, Any]) -> bool:
        pass

    @abstractmethod
    def get_airplanes(self, **criteria):
        pass

    @abstractmethod
    def delete_airplanes(self, **criteria):
        pass


class PlaneSaverJson(AirplaneStorage):
    """Класс для работы с файловой системой"""
    save_directory = Path(__file__).parent.parent / 'data'
    data_file = save_directory / 'planes_jsom.json'

    def __init__(self):
        self.file_path = Path(__file__)

    @classmethod
    def change_json(cls):
        """Метод для приведения информации из JSON к списку со словарями"""
        with open(cls.data_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            planes = data['planes']
        planes_list = []
        for plane in planes:
            unit = json.loads(plane)
            planes_list.append(unit)
        return planes_list

    def add_airplane(self, airplane: list):
        """Метод для добавления информации о самолетах в JSON файл"""
        save_directory = self.file_path.parent.parent / 'data'
        data_file = save_directory / 'planes_jsom.json'
        if not save_directory.exists():
            save_directory.mkdir()
        if not data_file.exists():
            data = {
                "planes" : []
            }
            data_file.touch()
            with open(data_file , 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)

        with open(data_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for plane in airplane:
                data["planes"].append(plane)

        with open(data_file, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def get_airplanes(self, criteria=None):
        """Метод для получения информации о самолетах в выбранных критериях(параметр рейса)"""
        planes_list = PlaneSaverJson.change_json()
        if criteria:
            filtered_planes = []
            for plane in planes_list:
                for value in plane.values():
                    if value.lower() == criteria.lower():
                        filtered_planes.append(plane)
            print(filtered_planes)
        else:
            print(planes_list)

    def delete_airplanes(self, criteria=None):
        """Метод для удаления информации о самолете по критерию(параметру рейса)"""
        planes_list = PlaneSaverJson.change_json()
        if criteria:
            new_planes_list = []
            for plane in planes_list:
                pattern = []
                for value in plane.values():
                    pattern.append(value.lower())
                if criteria.lower() not in pattern:
                    new_planes_list.append(plane)
                else:
                    continue
            with open(PlaneSaverJson.data_file, 'w', encoding='utf-8') as file:
                data = {
                    "planes": new_planes_list
                }
                json.dump(data, file, ensure_ascii=False)

            print(new_planes_list)
            return new_planes_list

        else:
            delete_all = input("Критерий отсутствует. Удалить всю информацию?\n"
                               "Да / Нет\n")
            if delete_all.lower() == 'да':
                data = {
                    "planes": []
                }
                with open(PlaneSaverJson.data_file, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False)
            elif delete_all.lower() == 'нет':
                print("Удаление отменено")
            else:
                print("Удаление отменено")
