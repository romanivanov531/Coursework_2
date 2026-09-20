from src.class_api import BasicAPI
from src.class_planes import Planes


def main():
    country = input('Введите страну\n')
    api = BasicAPI()
    coordinates = api.get_coordinates(country)
    planes_data = api.get_aeroplanes(coordinates)
    for plane in planes_data:
        Planes(plane)
    user_top_range = input("Выберите количество самолетов для составления топа по высоте полета\n"
                           "Например: 5\n")
    country_filter = input("Введите названия страны для фильтрации по стране регистрации: \n"
                           "Оставьте поле пустым, если фильтрация не нужна.\n")

    rating = Planes.compare_planes_by_geo_altitude(int(user_top_range), country_filter)
    for plane in rating:
        print(plane)


if __name__ == "__main__":
    main()
