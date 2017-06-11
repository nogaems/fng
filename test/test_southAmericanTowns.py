
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.southAmericanTowns import southAmericanTowns

value = list(southAmericanTowns.nameGen())

class southAmericanTowns(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
