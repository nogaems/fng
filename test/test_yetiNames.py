
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.yetiNames import yetiNames

value = list(yetiNames.nameGen())

class yetiNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
