
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.pathfinderSylph import pathfinderSylph

value = list(pathfinderSylph.nameGen())

class pathfinderSylph(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
