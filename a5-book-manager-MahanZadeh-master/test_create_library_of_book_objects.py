from unittest import TestCase
from books import Library, Book, create_library_of_book_objects


class TestCreateLibraryOfBooks(TestCase):

    def test_number_of_books_in_library_matches_number_of_list_items(self):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'},
                          {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',
                           'subject': 'Life'}]
        actual = create_library_of_book_objects(test_book_list)
        self.assertEqual(2, len(actual.libraries))

    def test_library_contains_book_objects(self):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'},
                          {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',
                           'subject': 'Life'}]
        actual = create_library_of_book_objects(test_book_list)
        for item in actual.libraries:
            self.assertTrue(type(item) is Book)

    def test_author_value_in_list_same_as_author_attribute_in_book_inside_library(self):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'},
                          {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',
                           'subject': 'Life'}]
        actual = create_library_of_book_objects(test_book_list)
        self.assertEqual(test_book_list[0]['author'], actual.libraries[0].author)

    def test_title_value_in_list_same_as_author_attribute_in_book_inside_library(self):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'},
                          {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',
                           'subject': 'Life'}]
        actual = create_library_of_book_objects(test_book_list)
        self.assertEqual(test_book_list[0]['title'], actual.libraries[0].title)

    def test_publisher_value_in_list_same_as_author_attribute_in_book_inside_library(self):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'},
                          {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',
                           'subject': 'Life'}]
        actual = create_library_of_book_objects(test_book_list)
        self.assertEqual(test_book_list[0]['publisher'], actual.libraries[0].publisher)

    def test_shelf_value_in_list_same_as_author_attribute_in_book_inside_library(self):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'},
                          {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',
                           'subject': 'Life'}]
        actual = create_library_of_book_objects(test_book_list)
        self.assertEqual(test_book_list[0]['shelf'], actual.libraries[0].shelf)

    def test_category_value_in_list_same_as_author_attribute_in_book_inside_library(self):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'},
                          {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',
                           'subject': 'Life'}]
        actual = create_library_of_book_objects(test_book_list)
        self.assertEqual(test_book_list[0]['category'], actual.libraries[0].category)

    def test_subject_value_in_list_same_as_author_attribute_in_book_inside_library(self):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'},
                          {'author': 'Chris', 'title': 'Smiles', 'publisher': 'Self', 'shelf': '2', 'category': 'Life',
                           'subject': 'Life'}]
        actual = create_library_of_book_objects(test_book_list)
        self.assertEqual(test_book_list[0]['subject'], actual.libraries[0].subject)
