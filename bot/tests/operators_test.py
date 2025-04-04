import unittest
import os
import sys


script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
from src.operators import search_query


class OperatorsTest(unittest.TestCase):
    def test_search_query(self):
        # given
        message = "the scp-14 is so beautifull!!"

        # then - when
        result = search_query(message)
        self.assertEqual(result, '014')

    def test_search_query2(self):
        # given
        message = "you should not detect me scp-test"

        # then - when
        result = search_query(message)
        self.assertEqual(result, '-1')

if __name__ == '__main__':
    unittest.main()
