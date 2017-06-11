
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.religionNames import religionNames

value = list(religionNames.nameGen())

class religionNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
