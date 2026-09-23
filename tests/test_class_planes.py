import unittest

from src.class_planes import Planes


class TestPlanes(unittest.TestCase):
    def setUp(self):
        self.plane_data1 = {
            'unique_id': 'A123',
            'registration': 'RU',
            'callsign': 'Flight 101',
            'velocity': 250,
            'geo_altitude': 3000,
            'on_ground': False
        }
        self.plane_data2 = {
            'unique_id': 'B456',
            'registration': 'US',
            'callsign': 'Flight 202',
            'velocity': 300,
            'geo_altitude': 5000,
            'on_ground': False
        }
        self.plane_data3 = {
            'unique_id': 'C789',
            'registration': 'RU',
            'callsign': 'Flight 303',
            'velocity': 200,
            'geo_altitude': 4000,
            'on_ground': False
        }
        Planes.planes_list11.clear()

    def test_plane_initialization(self):
        plane = Planes(self.plane_data1)
        self.assertEqual(plane.unique_id, 'A123')
        self.assertEqual(plane.registration, 'RU')
        self.assertEqual(plane.callsign, 'Flight 101')
        self.assertEqual(plane.velocity, 250)
        self.assertEqual(plane.geo_altitude, 3000)

    def test_compare_planes_by_velocity(self):
        Planes(self.plane_data1)
        Planes(self.plane_data2)
        Planes(self.plane_data3)
        sorted_planes = Planes.compare_planes_by_velocity(2)
        self.assertEqual(sorted_planes[0].unique_id, 'B456')
        self.assertEqual(sorted_planes[1].unique_id, 'A123')

    def test_compare_planes_by_geo_altitude(self):
        Planes(self.plane_data1)
        Planes(self.plane_data2)
        Planes(self.plane_data3)
        sorted_planes = Planes.compare_planes_by_geo_altitude(2)
        self.assertEqual(sorted_planes[0].unique_id, 'B456')
        self.assertEqual(sorted_planes[1].unique_id, 'C789')

    def test_compare_planes_by_geo_altitude_with_country(self):
        Planes(self.plane_data1)
        Planes(self.plane_data2)
        Planes(self.plane_data3)
        sorted_planes = Planes.compare_planes_by_geo_altitude(1, country='RU')
        self.assertEqual(sorted_planes[0].unique_id, 'C789')

    def test_error_on_invalid_data(self):
        with self.assertRaises(TypeError):
            Planes([])
