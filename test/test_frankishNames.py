
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.frankishNames import frankishNames

value = list(frankishNames.nameGen())

class frankishNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
