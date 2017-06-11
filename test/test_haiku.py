
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.haiku import haiku

value = list(haiku.nameGen())

class haiku(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
