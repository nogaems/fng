
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.starTrekBajorans import starTrekBajorans

value = list(starTrekBajorans.nameGen())

class starTrekBajorans(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
