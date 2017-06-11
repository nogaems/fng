
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.swEwokNames import swEwokNames

value = list(swEwokNames.nameGen())

class swEwokNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
