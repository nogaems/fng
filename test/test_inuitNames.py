
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.inuitNames import inuitNames

value = list(inuitNames.nameGen())

class inuitNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
