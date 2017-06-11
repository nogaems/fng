
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.zeldaGerudoNames import zeldaGerudoNames

value = list(zeldaGerudoNames.nameGen())

class zeldaGerudoNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
