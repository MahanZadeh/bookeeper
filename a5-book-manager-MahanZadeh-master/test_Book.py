from unittest import TestCase
from books import Book


class TestBook(TestCase):

    def setUp(self):
        self.test_book = Book("Mahan", "Tears in the time of Corona", "Independent", "1", "Life", "Slice of Life")
        self.test_book_two = Book("Mahan", "Tears in the time of Corona", "Independent", "", "Life", "Slice of Life")

    def test_correct_string_gets_printed(self):
        expected = "Title: 'Tears in the time of Corona', Author: 'Mahan', Publisher: 'Independent', Category: " \
                   "'Life', Subject: 'Slice of Life', Shelf: '1'"
        self.assertEqual(str(self.test_book), expected)

    def test_correct_object_info_gets_printed(self):
        expected = 'Book(Mahan, Tears in the time of Corona, Independent, 1, Life, Slice of Life)'
        actual = repr(self.test_book)
        self.assertEqual(actual, expected)

    def test_change_shelf_updates_shelf_attribute_to_a_string(self):
        actual = self.test_book.change_shelf("2")
        self.assertEqual("2", actual.shelf)

    def test_change_shelf_updates_shelf_attribute_to_an_int(self):
        actual = self.test_book.change_shelf(2)
        self.assertEqual(2, actual.shelf)

    def test_change_shelf_updates_shelf_if_empty_string(self):
        actual = self.test_book_two.change_shelf(2)
        self.assertEqual(2, actual.shelf)

    def test_change_shelf_updates_shelf_to_empty_string(self):
        actual = self.test_book.change_shelf("")
        self.assertEqual("", actual.shelf)

    def test_acquire_author(self):
        actual = self.test_book.author
        expected = "Mahan"
        self.assertEqual(expected, actual)

    def test_acquire_title(self):
        actual = self.test_book.title
        expected = "Tears in the time of Corona"
        self.assertEqual(expected, actual)

    def test_acquire_publisher(self):
        actual = self.test_book.publisher
        expected = "Independent"
        self.assertEqual(expected, actual)

    def test_acquire_shelf(self):
        actual = self.test_book.shelf
        expected = "1"
        self.assertEqual(expected, actual)

    def test_acquire_category(self):
        actual = self.test_book.category
        expected = "Life"
        self.assertEqual(expected, actual)

    def test_acquire_subject(self):
        actual = self.test_book.subject
        expected = "Slice of Life"
        self.assertEqual(expected, actual)
