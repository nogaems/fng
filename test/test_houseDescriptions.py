
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.houseDescriptions import houseDescriptions

value = list(houseDescriptions.nameGen())

class houseDescriptions(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
