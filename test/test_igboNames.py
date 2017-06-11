
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.igboNames import igboNames

value = list(igboNames.nameGen())

class igboNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
