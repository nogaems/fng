
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.zeldaHumanNames import zeldaHumanNames

value = list(zeldaHumanNames.nameGen())

class zeldaHumanNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
