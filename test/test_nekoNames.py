
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.nekoNames import nekoNames

value = list(nekoNames.nameGen())

class nekoNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
