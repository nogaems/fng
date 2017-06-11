
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.turkishNames import turkishNames

value = list(turkishNames.nameGen())

class turkishNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
