from unittest import TestCase
from unittest.mock import patch
import io
from books import perform_book_search
from books import Library
from books import Book


class TestPerformBookSearch(TestCase):

    @patch('builtins.input', return_value="Mahan")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_perform_book_search_by_author_when_provided_input_fully_matches(self, mock_output, mock_input):
        library_one = Library()
        book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        book_two = Book("Arian", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        library_one.add_books(book_one)
        library_one.add_books(book_two)
        actual = perform_book_search("1", library_one)
        expected = [book_one]
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="ian")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_perform_book_search_by_author_when_provided_input_partially_matches(self, mock_output, mock_input):
        library_one = Library()
        book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        book_two = Book("Arian", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        library_one.add_books(book_one)
        library_one.add_books(book_two)
        actual = perform_book_search("1", library_one)
        expected = [book_two]
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="ian")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_perform_book_search_returns_a_list(self, mock_output, mock_input):
        library_one = Library()
        book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        book_two = Book("Arian", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        library_one.add_books(book_one)
        library_one.add_books(book_two)
        actual = perform_book_search("1", library_one)
        self.assertTrue(type(actual) is list)

    @patch('builtins.input', return_value="Pie of Life")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_perform_book_search_by_subject_when_provided_input_fully_matches(self, mock_output, mock_input):
        library_one = Library()
        book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        book_two = Book("Arian", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        library_one.add_books(book_one)
        library_one.add_books(book_two)
        actual = perform_book_search("6", library_one)
        expected = [book_two]
        self.assertEqual(expected, actual)
