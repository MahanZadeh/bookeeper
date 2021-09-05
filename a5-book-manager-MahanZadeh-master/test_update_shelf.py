from unittest import TestCase
from unittest.mock import patch
import io
from books import update_shelf, Library, Book


class TestUpdateShelf(TestCase):

    @patch('builtins.input', side_effect=["1", "Mahan", "1", "new_shelf"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_shelf_updates_the_library_when_more_than_one_book_that_match_search_criteria(self, mock_output,
                                                                                                 mock_input):
        library_one = Library()
        book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        book_two = Book("Arian", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        book_three = Book("Mahan", "Some book", "Some publisher", "3", "Life", "Slice of Life")
        library_one.add_books(book_one)
        library_one.add_books(book_two)
        library_one.add_books(book_three)
        update_shelf(library_one)
        self.assertTrue(library_one.libraries[0].shelf == "new_shelf")

    @patch('builtins.input', side_effect=["1", "Mahan", "1", 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_shelf_updates_the_library_with_an_integer_as_new_shelf(self, mock_output, mock_input):
        library_one = Library()
        book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        book_two = Book("Arian", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        book_three = Book("Mahan", "Some book", "Some publisher", "3", "Life", "Slice of Life")
        library_one.add_books(book_one)
        library_one.add_books(book_two)
        library_one.add_books(book_three)
        update_shelf(library_one)
        self.assertTrue(library_one.libraries[0].shelf == 2)

    @patch('builtins.input', side_effect=["1", "Mahan", "1", 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_shelf_does_not_change_other_books_with_same_author(self, mock_output, mock_input):
        library_one = Library()
        book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        book_two = Book("Arian", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        book_three = Book("Mahan", "Some book", "Some publisher", "3", "Life", "Slice of Life")
        library_one.add_books(book_one)
        library_one.add_books(book_two)
        library_one.add_books(book_three)
        update_shelf(library_one)
        self.assertTrue(library_one.libraries[2] == book_three)

    @patch('builtins.input', side_effect=["1", "Mahan", "1", 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_shelf_returns_a_library(self, mock_output, mock_input):
        library_one = Library()
        book_one = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        book_two = Book("Arian", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        book_three = Book("Mahan", "Some book", "Some publisher", "3", "Life", "Slice of Life")
        library_one.add_books(book_one)
        library_one.add_books(book_two)
        library_one.add_books(book_three)
        actual = update_shelf(library_one)
        self.assertTrue(type(actual) is Library)
