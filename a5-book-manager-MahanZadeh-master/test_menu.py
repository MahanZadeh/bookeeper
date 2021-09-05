from unittest import TestCase
from unittest.mock import patch
import io
from books import menu


class TestMenu(TestCase):

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_with_1_as_input(self, mock_output, mock_input):
        actual = menu()
        expected = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="2")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_with_2_as_input(self, mock_output, mock_input):
        actual = menu()
        expected = "2"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_with_3_as_input(self, mock_output, mock_input):
        actual = menu()
        expected = "3"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_returns_string(self, mock_output, mock_input):
        actual = menu()
        self.assertTrue(type(actual) is str)
