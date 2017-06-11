
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.orcNames import orcNames

value = list(orcNames.nameGen())

class orcNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
