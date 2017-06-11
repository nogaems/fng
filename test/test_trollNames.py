
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.trollNames import trollNames

value = list(trollNames.nameGen())

class trollNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
