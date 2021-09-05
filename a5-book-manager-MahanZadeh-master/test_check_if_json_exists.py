import json
from unittest import TestCase
from unittest.mock import patch, mock_open
from books import check_if_json_exists


class TestCheckIfJsonExists(TestCase):

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='{"author": "Mahan"}')
    def test_when_json_exists(self, mock_file, mock_path):
        actual = check_if_json_exists()
        test_json = {"author": "Mahan"}
        test_json_file = json.dumps(test_json, ensure_ascii=False)
        with open(test_json_file) as json_file:
            expected = json.load(json_file)
        self.assertEqual(expected, actual)
