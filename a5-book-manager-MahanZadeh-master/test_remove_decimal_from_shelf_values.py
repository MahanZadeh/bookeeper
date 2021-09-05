from unittest import TestCase
from books import remove_decimal_from_shelf_values


class TestRemoveDecimalFromShelfValues(TestCase):

    def test_decimal_is_removed_from_string(self):
        test_book_list = [{'author': 'Mahan', 'shelf': '2.0'}]
        remove_decimal_from_shelf_values(test_book_list)
        self.assertEqual('2', test_book_list[0]['shelf'])

    def test_no_change_when_shelf_value_does_not_end_with_decimal(self):
        test_book_list = [{'author': 'Mahan', 'shelf': '2'}]
        remove_decimal_from_shelf_values(test_book_list)
        self.assertEqual('2', test_book_list[0]['shelf'])

    def test_no_change_when_shelf_value_is_alphabetical(self):
        test_book_list = [{'author': 'Mahan', 'shelf': 'Reading'}]
        remove_decimal_from_shelf_values(test_book_list)
        self.assertEqual('Reading', test_book_list[0]['shelf'])

    def test_a_list_is_returned(self):
        test_book_list = [{'author': 'Mahan', 'shelf': '2.0'}]
        actual = remove_decimal_from_shelf_values(test_book_list)
        self.assertTrue(type(actual) is list)

    def test_returned_list_contains_dicts(self):
        test_book_list = [{'author': 'Mahan', 'shelf': '2.0'}, {'author': 'Chris', 'shelf': 'Reading'}]
        actual = remove_decimal_from_shelf_values(test_book_list)
        for items in actual:
            self.assertTrue(type(items) is dict)
