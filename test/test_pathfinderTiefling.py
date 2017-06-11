
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.pathfinderTiefling import pathfinderTiefling

value = list(pathfinderTiefling.nameGen())

class pathfinderTiefling(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
