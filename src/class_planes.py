

class Planes:

    registration: str #Страна регистрации ВС
    unique_id: str #уникальный идентификатор борта
    callsign: str #позывной рейса
    velocity: str #горизонтальная скорость (м/с)
    geo_altitude: str #геометрическая высота (м)
    on_grond: str #находится ли самолёт на земле
    planes_list = []

    def __init__(self, data: dict):

        if isinstance(data, dict):
            self.unique_id = data['unique_id']
            self.registration = data['registration']
            self.callsign = data['callsign']
            self.velocity = data['velocity']
            self.geo_altitude = data['geo_altitude']
            self.on_ground = data['on_ground']
            Planes.planes_list.append(self)
        else:
            raise TypeError('Неверный тип данных. Ожидается тип данных Dict\n')
        for key,value in data.items():
            pattern = ['', ' ']
            if value in pattern:
                raise ValueError(f'Ошибка: значение отсутствует\n'
                                 f'Ключ: {key} должен быть заполнен.\n')

    def __str__(self):
        return (f'{"="*10}\n'
                f'Уникальный ID: {self.unique_id}\n'
                f'Позывной рейса: {self.callsign}\n'
                f'Скорость: {self.velocity}\n'
                f'Высота: {self.geo_altitude}')

    @classmethod
    def compare_planes_by_velocity(cls):
        rating = sorted(cls.planes_list, key=lambda x: x.velocity, reverse=True)
        for plane in rating:
            print(plane)

    @classmethod
    def compare_planes_by_geo_altitude(cls):
        rating = sorted(cls.planes_list, key=lambda x: x.geo_altitude, reverse=True)
        for plane in rating:
            print(plane)



# if __name__ == "__main__":
#
#     date = {'time': 1788078910, 'states': [
#     ['471d61', 'WZZ128  ', 'Hungary', 1788078849, 1788078851, 41.5138, 40.3862, 10668, False, 229.18, 115.53, 0, None, 11071.86, '4257', False, 0],
#     ['300a5c', 'LSI220  ', 'Italy', 1788078910, 1788078910, 42.3571, 40.9072, 10363.2, False, 250.46, 273.41, 0, None, 10767.06, '1305', False, 0],
#     ['a77f26', 'UPS11   ', 'United States', 1788078910, 1788078910, 45.463, 40.7706, 10363.2, False, 234.79, 272.39, 0, None, 10774.68, '0136', False, 0],
#     ['4bb274', 'THY77T  ', 'Turkey', 1788078910, 1788078910, 44.001, 40.8298, 10363.2, False, 225.05, 272.62, 0.33, None, 10797.54, '1315', False, 0],
#     ['4bb206', 'THY353  ', 'Turkey', 1788078769, 1788078770, 42.0153, 40.3964, 10370.82, False, 225.09, 276.17, 0, None, 10782.3, '3421', False, 0]
#       ]
#         }
#
#
#
#     for plan in date['states']:
#         id = Planes({
#             'unique_id' : plan[0],
#             'registration' : plan[2],
#             'callsign' : plan[1],
#             'velocity' : plan[9],
#             'geo_altitude' : plan[13],
#             'on_ground' : plan[8]
#         })
#
#     print(Planes)
#     # print([f'{plane.velocity} {plane.unique_id} {plane.__str__()}'  for plane in Planes.planes_list])
#     Planes.compare_planes_by_geo_altitude()