import json
import unittest
from unittest.mock import mock_open, patch

from src.class_save_data import PlaneSaverJson


class TestPlaneSaverJson(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.load')
    @patch('json.dump')
    def test_change_json(self, mock_json_dump, mock_json_load, mock_open):
        mock_json_load.return_value = {'planes': [json.dumps({"unique_id": "A123", "callsign": "Flight 101"})]}
        plane_saver = PlaneSaverJson()
        result = plane_saver.change_json()
        expected_result = [{"unique_id": "A123", "callsign": "Flight 101"}]
        self.assertEqual(result, expected_result)
