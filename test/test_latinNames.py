
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.latinNames import latinNames

value = list(latinNames.nameGen())

class latinNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
