from unittest import TestCase
from unittest.mock import patch
import io
from books import search_criteria


class TestSearchCriteria(TestCase):

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_criteria_with_1_as_input(self, mock_output, mock_input):
        actual = search_criteria()
        expected = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="2")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_criteria_with_2_as_input(self, mock_output, mock_input):
        actual = search_criteria()
        expected = "2"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_criteria_with_3_as_input(self, mock_output, mock_input):
        actual = search_criteria()
        expected = "3"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="4")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_criteria_with_4_as_input(self, mock_output, mock_input):
        actual = search_criteria()
        expected = "4"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="5")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_criteria_with_5_as_input(self, mock_output, mock_input):
        actual = search_criteria()
        expected = "5"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="6")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_criteria_with_6_as_input(self, mock_output, mock_input):
        actual = search_criteria()
        expected = "6"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_criteria_returns_string(self, mock_output, mock_input):
        actual = search_criteria()
        self.assertTrue(type(actual) is str)
