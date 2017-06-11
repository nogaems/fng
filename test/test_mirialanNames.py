
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.mirialanNames import mirialanNames

value = list(mirialanNames.nameGen())

class mirialanNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
