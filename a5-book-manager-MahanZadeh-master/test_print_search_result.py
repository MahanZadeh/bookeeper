from unittest import TestCase
from books import print_search_result
import io
from unittest.mock import patch


class TestPrintSearchResult(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_search_result_correct_output(self, mock_output):
        test_book_list = [{'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life',
                           'subject': 'Life'}]
        print_search_result(test_book_list)
        actual = mock_output.getvalue()
        expected = """There are 1 books that match your search criteria:\n
(1)-- {'author': 'Mahan', 'title': 'Tears', 'publisher': 'Self', 'shelf': '1', 'category': 'Life', 'subject': 'Life'}\n"""
        self.assertEqual(expected, actual)
