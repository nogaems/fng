
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.continentNames import continentNames

value = list(continentNames.nameGen())

class continentNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
