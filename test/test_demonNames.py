
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.demonNames import demonNames

value = list(demonNames.nameGen())

class demonNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
