from unittest import TestCase
from unittest.mock import patch, mock_open
from books import open_json_file


class TestOpenJsonFile(TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"author":"mahan"}, {"author":"chris"}]')
    def test_open_json_file_returns_a_list(self, mock_json):
        actual = open_json_file()
        self.assertTrue(type(actual) is list)

    @patch('builtins.open', new_callable=mock_open, read_data='[{"author":"mahan"}, {"author":"chris"}]')
    def test_correct_length_of_returned_list(self, mock_json):
        actual = open_json_file()
        self.assertEqual(2, len(actual))

    @patch('builtins.open', new_callable=mock_open, read_data='[{"author":"mahan"}, {"author":"chris"}]')
    def test_list_items_are_dicts(self, mock_json):
        actual = open_json_file()
        for item in actual:
            self.assertTrue(type(item) is dict)
