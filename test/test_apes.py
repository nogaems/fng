
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.apes import apes

value = list(apes.nameGen())

class apes(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
