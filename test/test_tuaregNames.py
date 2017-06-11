
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.tuaregNames import tuaregNames

value = list(tuaregNames.nameGen())

class tuaregNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
