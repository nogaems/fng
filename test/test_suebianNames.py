
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.suebianNames import suebianNames

value = list(suebianNames.nameGen())

class suebianNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
