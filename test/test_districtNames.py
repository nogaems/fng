
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.districtNames import districtNames

value = list(districtNames.nameGen())

class districtNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
