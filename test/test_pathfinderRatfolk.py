
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.pathfinderRatfolk import pathfinderRatfolk

value = list(pathfinderRatfolk.nameGen())

class pathfinderRatfolk(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
