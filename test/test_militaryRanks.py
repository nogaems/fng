
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.militaryRanks import militaryRanks

value = list(militaryRanks.nameGen())

class militaryRanks(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
