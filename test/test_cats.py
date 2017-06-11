
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.cats import cats

value = list(cats.nameGen())

class cats(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
