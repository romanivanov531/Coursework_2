import unittest
from unittest.mock import Mock, patch

from src.class_api import BasicAPI


class TestBasicAPI(unittest.TestCase):
    def setUp(self):
        self.api = BasicAPI()

    @patch('src.class_api.requests.get')
    def test_get_coordinates(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [{'boundingbox': ['10.0', '20.0', '30.0', '40.0']}]
        mock_get.return_value = mock_response

        coordinates = self.api.get_coordinates('Russia')
        self.assertEqual(coordinates, ['10.0', '20.0', '30.0', '40.0'])

    @patch('src.class_api.requests.get')
    def test_get_aeroplanes(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            'states': [
                ['A123', 'Flight 101', 'RU', '...', 0, 0, 0, 0, 1, 250, 0, 0, 0, 3000],
                ['B456', 'Flight 202', 'US', '...', 0, 0, 0, 0, 0, 300, 0, 0, 0, 5000]
            ]
        }
        mock_get.return_value = mock_response

        coordinates = ['10.0', '20.0', '30.0', '40.0']
        planes = self.api.get_aeroplanes(coordinates)

        expected_planes = [
            {'unique_id': 'A123', 'registration': 'RU', 'callsign': 'Flight 101', 'velocity': 250,
             'geo_altitude': 3000, 'on_ground': 1},
            {'unique_id': 'B456', 'registration': 'US', 'callsign': 'Flight 202', 'velocity': 300,
             'geo_altitude': 5000, 'on_ground': 0}
        ]
        self.assertEqual(planes, expected_planes)
