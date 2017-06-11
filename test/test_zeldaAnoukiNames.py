
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.zeldaAnoukiNames import zeldaAnoukiNames

value = list(zeldaAnoukiNames.nameGen())

class zeldaAnoukiNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
