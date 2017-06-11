
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.zeldaMinishNames import zeldaMinishNames

value = list(zeldaMinishNames.nameGen())

class zeldaMinishNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
