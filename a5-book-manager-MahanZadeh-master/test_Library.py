from unittest import TestCase
from books import Book
from books import Library


class TestLibrary(TestCase):

    def setUp(self):
        self.test_book = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        self.test_book_two = Book("Mahan", "Hello world", "UK", "Reading", "Death", "Pie of Life")
        self.test_book_three = Book("Arian", "Bye world", "France", "4", "Limbo", "No pie")
        self.test_book_four = Book("Hamid", "This is world", "LalaLand", "44", "Purgatory", "Glass")
        self.test_library = Library()

    def test_correct_string_gets_printed(self):
        expected = '[Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)] contains 1 books.'
        self.test_library.add_books(self.test_book)
        self.assertEqual(str(self.test_library), expected)

    def test_correct_object_info_gets_printed(self):
        expected = 'Library([Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)])'
        self.test_library.add_books(self.test_book)
        actual = repr(self.test_library)
        self.assertEqual(actual, expected)

    def test_add_books_correctly_adds_to_library(self):
        self.test_library.add_books(self.test_book)
        self.assertTrue(self.test_book in self.test_library.libraries)

    def test_add_books_duplicate_books(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book)
        self.assertEqual(len(self.test_library.libraries), 2)

    def test_type_error_when_adding_integer(self):
        with self.assertRaises(TypeError):
            self.test_library.add_books(2)

    def test_type_error_when_adding_float(self):
        with self.assertRaises(TypeError):
            self.test_library.add_books(2.2)

    def test_type_error_when_adding_string(self):
        with self.assertRaises(TypeError):
            self.test_library.add_books("Mahan")

    def test_type_error_when_adding_list(self):
        with self.assertRaises(TypeError):
            self.test_library.add_books([])

    def test_type_error_when_adding_dictionary(self):
        with self.assertRaises(TypeError):
            self.test_library.add_books({'key': 2})

    def test_update_library_with_string_as_shelf(self):
        self.test_library.add_books(self.test_book)
        self.test_library.update_library(self.test_book, "33")
        self.assertEqual("33", self.test_book.shelf)

    def test_update_library_shelf_of_correct_book_is_updated(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.update_library(self.test_book, 2)
        self.assertEqual(2, self.test_book.shelf)

    def test_search_library_by_author_correct_list_of_results_returned(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_author("Mahan")
        expected = [self.test_book, self.test_book_two]
        self.assertEqual(expected, actual)

    def test_search_library_by_author_correct_list_of_results_returned_regardless_of_case(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_author("mahan")
        expected = [self.test_book, self.test_book_two]
        self.assertEqual(expected, actual)

    def test_search_library_by_author_correct_list_of_results_returned_with_partial_info(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_author("han")
        expected = [self.test_book, self.test_book_two]
        self.assertEqual(expected, actual)

    def test_search_library_by_author_empty_list_returned_when_no_match(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_author("Chris")
        expected = []
        self.assertEqual(expected, actual)

    def test_search_library_by_author_when_there_are_leading_trailing_whitespaces(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_author(" mahan   ")
        expected = [self.test_book, self.test_book_two]
        self.assertEqual(expected, actual)

    def test_search_library_by_title_correct_list_of_results_returned(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_title("Tears in the time of Corona")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_title_correct_list_of_results_returned_regardless_of_case(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_title("TEARS IN THE TIME OF CORONA")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_title_correct_list_of_results_returned_with_partial_info(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_title("time")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_title_empty_list_returned_when_no_match(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_title("Blue Lake")
        expected = []
        self.assertEqual(expected, actual)

    def test_search_library_by_title_when_there_are_leading_trailing_whitespaces(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_title(" bye   ")
        expected = [self.test_book_three]
        self.assertEqual(expected, actual)

    def test_search_library_by_publisher_correct_list_of_results_returned(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_publisher("Independent")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_publisher_correct_list_of_results_returned_regardless_of_case(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_publisher("iNdEpendent")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_publisher_correct_list_of_results_returned_with_partial_info(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_publisher("pendent")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_publisher_empty_list_returned_when_no_match(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_publisher("Iran")
        expected = []
        self.assertEqual(expected, actual)

    def test_search_library_by_publisher_when_there_are_leading_trailing_whitespaces(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_publisher(" UK   ")
        expected = [self.test_book_two]
        self.assertEqual(expected, actual)

    def test_search_library_by_shelf_correct_list_of_results_returned(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_shelf("1")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_shelf_correct_list_of_results_returned_regardless_of_case(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_shelf("rEading")
        expected = [self.test_book_two]
        self.assertEqual(expected, actual)

    def test_search_library_by_shelf_correct_list_of_results_returned_only_when_characters_fully_match(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        self.test_library.add_books(self.test_book_four)
        actual = self.test_library.search_library_by_shelf("4")
        expected = [self.test_book_three]
        self.assertEqual(expected, actual)

    def test_search_library_by_shelf_empty_list_returned_when_no_match(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_shelf("33")
        expected = []
        self.assertEqual(expected, actual)

    def test_search_library_by_shelf_when_there_are_leading_trailing_whitespaces(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_shelf(" reading   ")
        expected = [self.test_book_two]
        self.assertEqual(expected, actual)

    def test_search_library_by_category_correct_list_of_results_returned(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_category("Life")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_category_correct_list_of_results_returned_regardless_of_case(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_category("lIfE")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_categroy_correct_list_of_results_returned_with_partial_info(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        self.test_library.add_books(self.test_book_four)
        actual = self.test_library.search_library_by_category("eath")
        expected = [self.test_book_two]
        self.assertEqual(expected, actual)

    def test_search_library_by_category_empty_list_returned_when_no_match(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_shelf("Hell")
        expected = []
        self.assertEqual(expected, actual)

    def test_search_library_by_category_when_there_are_leading_trailing_whitespaces(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_category(" limbo   ")
        expected = [self.test_book_three]
        self.assertEqual(expected, actual)

    def test_search_library_by_subject_correct_list_of_results_returned(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_subject("No Pie")
        expected = [self.test_book_three]
        self.assertEqual(expected, actual)

    def test_search_library_by_subject_correct_list_of_results_returned_regardless_of_case(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_subject("slice OF lIFE")
        expected = [self.test_book]
        self.assertEqual(expected, actual)

    def test_search_library_by_subject_correct_list_of_results_returned_with_partial_info(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        self.test_library.add_books(self.test_book_four)
        actual = self.test_library.search_library_by_subject("pie")
        expected = [self.test_book_two, self.test_book_three]
        self.assertEqual(expected, actual)

    def test_search_library_by_subject_empty_list_returned_when_no_match(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_subject("cake")
        expected = []
        self.assertEqual(expected, actual)

    def test_search_library_by_subject_when_there_are_leading_trailing_whitespaces(self):
        self.test_library.add_books(self.test_book)
        self.test_library.add_books(self.test_book_two)
        self.test_library.add_books(self.test_book_three)
        actual = self.test_library.search_library_by_subject(" No pie   ")
        expected = [self.test_book_three]
        self.assertEqual(expected, actual)
