
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.uzbekNames import uzbekNames

value = list(uzbekNames.nameGen())

class uzbekNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
