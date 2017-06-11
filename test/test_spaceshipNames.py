
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.spaceshipNames import spaceshipNames

value = list(spaceshipNames.nameGen())

class spaceshipNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
