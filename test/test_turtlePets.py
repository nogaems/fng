
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.turtlePets import turtlePets

value = list(turtlePets.nameGen())

class turtlePets(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
