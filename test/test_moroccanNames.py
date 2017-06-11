
import unittest
import sys, os
sys.path.append(os.path.abspath('.'))
from generators.moroccanNames import moroccanNames

value = list(moroccanNames.nameGen())

class moroccanNames(unittest.TestCase):

    def test_name_gen_non_empty(self):
        self.assertTrue(len(value) != 0)

if __name__ == "__main__":
    unittest.main()
