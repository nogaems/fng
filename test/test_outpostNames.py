
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.outpostNames import outpostNames

value = list(outpostNames.nameGen())

class outpostNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
