
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.fantasyFood import fantasyFood

value = list(fantasyFood.nameGen())

class fantasyFood(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
