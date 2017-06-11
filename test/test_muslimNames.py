
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.muslimNames import muslimNames

value = list(muslimNames.nameGen())

class muslimNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
