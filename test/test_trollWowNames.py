
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.trollWowNames import trollWowNames

value = list(trollWowNames.nameGen())

class trollWowNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
