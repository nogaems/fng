
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.somalianNames import somalianNames

value = list(somalianNames.nameGen())

class somalianNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
